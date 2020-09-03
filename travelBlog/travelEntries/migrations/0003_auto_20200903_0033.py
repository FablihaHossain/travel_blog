# Generated by Django 3.0.3 on 2020-09-03 00:33

import django.core.validators
from django.db import migrations, models
import travelEntries.models


class Migration(migrations.Migration):

    dependencies = [
        ('travelEntries', '0002_auto_20200816_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='numOfDescriptions',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entryimage',
            name='image',
            field=models.ImageField(upload_to=travelEntries.models.EntryImage.get_upload_path),
        ),
    ]
