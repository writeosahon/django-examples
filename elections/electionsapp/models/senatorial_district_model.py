from django.db import models

# Create your models here.

class SenatorialDistrict(models.Model):
    senatorial_id = models.BigAutoField(primary_key=True, help_text="Auto Increament primary key", 
                                        editable=False)
    senatorial_district_name = models.CharField(help_text="District Name", max_length=255,
                                null=False, blank=False, unique=True, verbose_name="District Name")
    
    def __str__(self):
        return (self.senatorial_district_name)

    class Meta:
        managed = True
        ordering = ["senatorial_district_name"]
        verbose_name = 'Senatorial District'
        verbose_name_plural = 'Senatorial Districts'
