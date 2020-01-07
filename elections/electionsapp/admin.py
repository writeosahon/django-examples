from django.contrib import admin

from .models import senatorial_district_model
from .models import lga_model
from .models import voter_model

# Register your models here.

admin.site.register(lga_model.Lga)
admin.site.register(senatorial_district_model.SenatorialDistrict)
admin.site.register(voter_model.Voter)
