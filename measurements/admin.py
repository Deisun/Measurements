from django.contrib import admin
from .models import Area, Category, Location

class LocationInLine(admin.TabularInline):
    model = Location


class AreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['id']}),
        (None, {'fields' : ['name']}),
        (None, {'fields' : ['longitude']}),
        (None, {'fields' : ['latitude']}),
        ]

    inlines = [LocationInLine]


class CategoryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass





admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

