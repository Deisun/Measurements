__author__ = 'faculty'

from measurements.models import Area, Category, Location, Measurement

import random
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "adds sample entities to the application"

    def handle(self, *args, **options):

        area_data = [
            [1, "Grand Canyon", 20, 30],
            [2, "Boca Raton", 40, 50],
            [3, "Kennesaw", 60, 70],
            [4, "Mount Hood", 80, 90],
            [5, "Mount Rainer", 46.5, 121.5],
            [6, "Saint Olaf", 44, 93],
            [7, "Mount St. Helens", 46, 122]
        ]

        for ad in area_data:
            a = Area(name=ad[1], id=ad[0], longitude=ad[2], latitude=ad[3])
            a.save()

        location_data = [
            [11, "South rim", 200, 1],
            [12, "North rim", 300, 1],
            [13, "Phantom Ranch", 100, 1],
            [14, "Waterfront", 10, 2],
            [15, "Town center", 15, 2],
            [16, "Town center", 310, 3],
            [17, "University", 320, 3],
            [18, "Mall", 330, 3],
            [19, "Airport", 350, 3],
            [20, "South pass", 3500, 4],
            [21, "North rim", 4500, 4],
            [22, "Crater", 4000, 4],
            [23, "North pass", 14000, 5],
            [24, "South glacier", 15000, 5],
            [25, "Ranger station", 16000, 5],
            [26, "Summit", 17000, 5],
            [27, "Yttrboe", 250, 6],
            [28, "Science", 250, 6],
        ]

        no_measurements_location_ids = [23]

        for locd in location_data:
            loc = Location(id=locd[0], name=locd[1], altitude=locd[2])
            a = Area.objects.get(pk=locd[3])
            loc.area = a
            loc.save()

        category_data = [
            [31, "Volcanos", "Areas that are on volcanoes", [4, 5]],
            [32, "East", "Areas that are in the east", [2, 3]],
            [33, "West", "Areas that are in the west", [1, 4, 5]],
            [34, "Wetlands", "Areas that are wetlands", []]
            ]

        for catd in category_data:
            cat = Category(id=catd[0], name=catd[1], description=catd[2])
            cat.save()
            for memb_id in catd[3]:
                a = Area.objects.get(pk=memb_id)
                cat.members.add(a)
            cat.save()

        num_meas_per_loc = 10

        for locd in location_data:
            loc_id = locd[0]
            if loc_id not in no_measurements_location_ids:
                loc = Location.objects.get(pk=loc_id)
                for meas_id in range(loc_id*100, loc_id*100+num_meas_per_loc):
                    val = random.uniform(5+loc_id*3, 15+loc_id*3)
                    meas = Measurement(value=val, id=meas_id, date=timezone.now())
                    meas.location = loc
                    meas.save()
