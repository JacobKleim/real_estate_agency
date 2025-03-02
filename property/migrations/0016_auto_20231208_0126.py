# Generated by Django 2.2.24 on 2023-12-07 21:26

from django.db import migrations


def connect_owner_apartment(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.iterator():
        flats_to_connect = Flat.objects.filter(
            owner_pure_phone=owner.pure_phone)

        owner.flats.set(flats_to_connect)
        owner.save()


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.set = None
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20231208_0036'),
    ]

    operations = [
        migrations.RunPython(connect_owner_apartment, move_backward),
    ]
