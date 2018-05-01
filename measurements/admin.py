from django.contrib import admin
from .models import Area, Category, Location


class AreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['area'] } ),
        ]


class CategoryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass





admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

