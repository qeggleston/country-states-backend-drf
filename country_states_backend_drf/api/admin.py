from django.contrib import admin
from .models import Country, State

# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass

