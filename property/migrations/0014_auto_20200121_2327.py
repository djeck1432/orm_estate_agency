# Generated by Django 2.2.4 on 2020-01-21 20:27

from django.db import migrations, models
import phonenumbers

def phone_pure(apps,shema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        formated_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        flat.owner_phone_pure = formated_number
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20200121_2242'),
    ]

    operations = [
        migrations.RunPython(phone_pure)
    ]