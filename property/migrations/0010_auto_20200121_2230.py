# Generated by Django 2.2.4 on 2020-01-21 19:30

from django.db import migrations, models

def like(apps,shema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.like = ''


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20200121_2225'),
    ]

    operations = [
        migrations.RunPython(like)
    ]
