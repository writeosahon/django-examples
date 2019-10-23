from django.db import models

from . import senatorial_district_model 

# Create your models here.

class Lga(models.Model):
    lga_id = models.BigAutoField(primary_key=True, help_text="Auto Increament primary key", 
                                        editable=False)
    lga_name = models.CharField(help_text="LGA Name", max_length=255,
                                null=False, blank=False, unique=True)
    
    senatorial_district = models.ForeignKey(senatorial_district_model.SenatorialDistrict, 
                            help_text="senatorial district of lga", null=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return (self.lga_name)

    class Meta:
        managed = True
        verbose_name = 'LGA'
        verbose_name_plural = 'LGAs'
