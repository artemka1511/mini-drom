from django.contrib import admin

from cars.models import City, Brand, Model, Car, Images

admin.site.register(City)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Images)
