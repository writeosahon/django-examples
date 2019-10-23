from django.contrib import admin

from electionsapp.models import senatorial_district_model
from electionsapp.models import lga_model

# Register your models here.

admin.site.register(lga_model.Lga)
admin.site.register(senatorial_district_model.SenatorialDistrict)
