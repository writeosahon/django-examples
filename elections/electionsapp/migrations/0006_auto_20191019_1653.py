# Generated by Django 2.2.6 on 2019-10-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electionsapp', '0005_auto_20191019_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='senatorial_district',
            field=models.ForeignKey(help_text='senatorial district of lga', on_delete=django.db.models.deletion.PROTECT, to='electionsapp.SenatorialDistrict'),
        ),
    ]
