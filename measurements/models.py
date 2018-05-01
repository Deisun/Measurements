from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField
    latitude = models.FloatField

    def number_of_locations(self):
        # TODO implement this method
        pass

    def average_measurements(self):
        # TODO implement this method
        pass

    def category_names(self):
        # TODO implement this method
        pass

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=200)
    altitude = models.IntegerField
    area = models.ForeignKey(Area)

    def __str__(self):
        return self.area.name + ':' + self.name


class Measurement(models.Model):
    value = models.FloatField
    date = models.DateField
    location = models.ForeignKey(Location)

    def __str__(self):
        return 'measurement@' + self.location.__str__()


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField
    members = models.ManyToManyField(Area)

    def __str__(self):
        return self.name
