from django.db import models

class Area(models.Model):
    

    def __str__(self):
        return self.name
