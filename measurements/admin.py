from django.contrib import admin
from .models import Area, Category, Location, Measurement


class LocationInLine(admin.TabularInline):
    model = Location


class MeasurementInLine(admin.TabularInline):
    model = Measurement


class AreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['name']}),
        (None, {'fields' : ['longitude']}),
        (None, {'fields' : ['latitude']}),
        ]

    inlines = [LocationInLine]


class CategoryAdmin(admin.ModelAdmin):
    filter_vertical = ('members',)
    fields = ['name', 'members', 'description']


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['altitude']}),
        (None, {'fields' : ['area']}),
    ]

    inlines = [MeasurementInLine]


admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

