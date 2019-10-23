# Generated by Django 2.2.6 on 2019-10-19 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SenatorialDistrict',
            fields=[
                ('senatorial_id', models.BigAutoField(editable=False, help_text='Auto Increament primary key', primary_key=True, serialize=False)),
                ('senatorial_district_name', models.CharField(help_text='District Name', max_length=255, unique=True, verbose_name='District Name')),
            ],
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('lga_id', models.BigAutoField(editable=False, help_text='Auto Increament primary key', primary_key=True, serialize=False)),
                ('lga_name', models.CharField(help_text='LGA Name', max_length=255, unique=True)),
                ('senatorial_district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electionsapp.SenatorialDistrict')),
            ],
        ),
    ]
