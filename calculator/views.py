from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import *

def index(request):
    return render(request, 'index.html')

def zipcode_info(request):
    if request.method == "GET":
        zipcode_no = request.GET['zipcode']
        zipcode = Zipcode.objects.filter(zipcode=zipcode_no)

        json_data = None
        if len(zipcode) > 0:
            json_data = serializers.serialize('json', zipcode)

        print json_data

        return HttpResponse(json_data, content_type="application/json")
