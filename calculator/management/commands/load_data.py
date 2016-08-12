import csv
from calculator.models import *
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

  help = 'load database from csv'

  def handle(self, *args, **options):

    Zipcode.objects.all().delete()

    with open('calculator/static/zipcode_airbnb_earnings_vs_rent_data_for_calculator.csv', 'rb') as f:
      reader = csv.reader(f)

      row_count = 0
      first_row = True
      for row in reader:
        row_count += 1

        if first_row:
          first_row = False
          continue

        # check if zipcode exists already
        if len(Zipcode.objects.filter(zipcode=int(row[0]))) > 0:
          continue

        monthly_rent = None
        if row[3].strip().lower() != "na":
          monthly_rent = float(row[3])

        nightly_rev = None
        if row[4].strip().lower() != "na":
          nightly_rev = float(row[4])

        payoff_nights = None
        if row[5].strip().lower() != "na":
          payoff_nights = float(row[5])

        zipcode = Zipcode(
          zipcode=int(row[0]),
          cbsa=int(row[1]),
          cbsa_title=unicode(row[2], errors='replace'),
          monthly_rent=monthly_rent,
          nightly_rev=nightly_rev,
          payoff_nights=payoff_nights
        )

        print row_count
        zipcode.save()
