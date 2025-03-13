from django.contrib import admin
from .models import User, AutoPlate, Bid

@admin.register(AutoPlate)
class AutoPlateAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass