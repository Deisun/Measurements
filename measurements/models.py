import datetime
from django.db import models
from django.db.models import Avg


class Area(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def number_of_locations(self):
        return self.location_set.count()

    def average_measurements(self):
        result = self.location_set.aggregate(average=Avg('measurement__value'))
        return result

    def category_names(self):
        queryset = self.category_set.all()
        return queryset.values('name')

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    altitude = models.IntegerField(blank=True, null=True)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__(self):
        return self.area.name + ':' + self.name


class Measurement(models.Model):
    value = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return 'measurement@' + self.location.__str__()


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField('Area')

    def __str__(self):
        return self.name
