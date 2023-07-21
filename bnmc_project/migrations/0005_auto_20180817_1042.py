# Generated by Django 2.0.7 on 2018-08-17 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bnmc_project', '0004_auto_20180812_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_registration',
            name='approve_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approve_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='created_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student_registration',
            name='created_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='show_permission',
        ),
        migrations.AddField(
            model_name='user',
            name='show_permission',
            field=models.ManyToManyField(related_name='show_permission_permissions', to='bnmc_project.Permission'),
        ),
    ]
