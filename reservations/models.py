from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_public = models.BooleanField()

    def __str__(self):
        return self.username + ", " + self.email


class ParkingSpace(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    evidence_no = models.CharField(max_length=255)

    def __str__(self):
        return self.building + " - " + self.evidence_no


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    purpose = models.CharField(max_length=255)

    def is_active_reservation(self):
        return self.start_date <= timezone.now() <= self.end_date

    def __str__(self):
        return self.user.email + ", " + \
               self.parking_space.building + " " + \
               self.parking_space.evidence_no + \
               ", Active: " + str(self.is_active_reservation())
