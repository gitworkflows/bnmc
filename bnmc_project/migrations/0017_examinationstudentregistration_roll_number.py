# Generated by Django 2.1.1 on 2019-05-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0016_examinationstudentregistration_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinationstudentregistration',
            name='roll_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
