from django.contrib import admin

# Register your models here.
from .models import Car, InsurancePolicy, Make, Model

admin.site.register(Car)
admin.site.register(InsurancePolicy)
admin.site.register(Make)
admin.site.register(Model)