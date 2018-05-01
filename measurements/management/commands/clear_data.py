__author__ = 'faculty'

from measurements.models import Area, Category, Location, Measurement


from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = "adds sample entities to the application"

    def handle(self, *args, **options):
        Area.objects.all().delete()
        Category.objects.all().delete()

