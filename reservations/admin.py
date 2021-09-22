from django.contrib import admin

from .models import User, ParkingSpace, Reservation

admin.site.register(User)
admin.site.register(ParkingSpace)
admin.site.register(Reservation)