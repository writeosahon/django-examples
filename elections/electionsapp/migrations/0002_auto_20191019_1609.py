# Generated by Django 2.2.6 on 2019-10-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electionsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='lga_name',
            field=models.CharField(help_text='LGA Name', max_length=254, unique=True),
        ),
    ]
