from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import get_template

from .models import *

def index(request):
    zipcode_boundary_points = ZipcodeBoundaryPoint.objects.all()
    zipcode_bounds = {}

    for point in zipcode_boundary_points:
      latlng = [float(point.lat), float(point.lng)]
      zipcode_bounds.setdefault(int(point.zipcode), []).append(latlng)

    zipcode_bounds_list = [[zipcode, zipcode_bounds[zipcode]] for zipcode in zipcode_bounds]

    context = { "dc_polygons": zipcode_bounds_list }

    return render(request, 'index.html', context)


def cbsa_from_zipcode(request):
    if request.method == "GET":
        zipcode_no = request.GET['zipcode']
        cbsa = Zipcode.objects.values("cbsa").filter(zipcode=zipcode_no).values_list('cbsa',flat=True)
        list_zipcode_from_cbsa = Zipcode.objects.filter(cbsa=cbsa[0])
        zipcodes = set(zip.zipcode for zip in list_zipcode_from_cbsa)
        zipcode_boundaries = ZipcodeBoundaryPoint.objects.filter(zipcode__in=zipcodes)

        json_data = None
        if len(zipcode_boundaries) > 0:
              json_data = serializers.serialize('json', zipcode_boundaries)

        return HttpResponse(json_data, content_type="application/json")

def zipcode_info(request):
    if request.method == "GET":
        zipcode_no = request.GET['zipcode']
        zipcode = Zipcode.objects.filter(zipcode=zipcode_no)

        print zipcode

        json_data = None
        if len(zipcode) > 0:
            json_data = serializers.serialize('json', zipcode)

        print json_data

        return HttpResponse(json_data, content_type="application/json")

def bounds_info(request):
  if request.method == "GET":
    zipcode_no = request.GET['zipcode']
    points = ZipcodeBoundaryPoint.objects.filter(zipcode=zipcode_no)

    json_data = None
    if len(points) > 0:
      json_data = serializers.serialize('json', points)

    print json_data

    return HttpResponse(json_data, content_type="application/json")
