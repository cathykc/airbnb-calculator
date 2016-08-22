import csv
from calculator.models import *
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

  help = 'load database from csv'

  def geom_filter_float(self, s):
    return float(filter(lambda x: x in ',.-0123456789', s))

  def handle(self, *args, **options):
    zipcodes = {}
    row_count = 0

    with open('US-ZIP codes-filtered.csv', 'rb') as zipcodefile:
      csvreader = csv.reader(zipcodefile)
      next(csvreader)

      for row in csvreader:
        # Skip if zipcode already in db
        if len(ZipcodeBoundaryPoint.objects.filter(zipcode=int(row[3]))) > 0:
          continue

        raw_bounds = row[11].split()
        str_bounds = [coords.split(',')[:-1] for coords in raw_bounds]
        # Convert to lat, lng
        bounds = [[self.geom_filter_float(coords[1]), self.geom_filter_float(coords[0])] for coords in str_bounds]

        for i, point in enumerate(bounds):
          zipcode_boundary_point = ZipcodeBoundaryPoint(
            zipcode = int(row[3]),
            lat = point[0],
            lng = point[1],
            order_in_boundary = i
          )

          zipcode_boundary_point.save()
          row_count += 1

    print row_count





