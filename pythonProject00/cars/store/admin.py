from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Car)

