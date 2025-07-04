from django.contrib import admin
from cars.models import Car, Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)

