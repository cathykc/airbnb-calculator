from django.db import models

# Create your models here.
class Zipcode(models.Model):
  zipcode = models.IntegerField(null=False, blank=False, unique=True)
  cbsa = models.IntegerField(null=False, blank=False)
  cbsa_title = models.CharField(null=False, blank=False, max_length=255)
  monthly_rent = models.FloatField()
  nightly_rev = models.FloatField()
  payoff_nights = models.FloatField()
