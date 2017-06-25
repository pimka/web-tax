from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)

class UserResults(models.Model):
    #IDuser = models.OneToOneField(User)
    IDuser = models.ForeignKey('auth.User')
    number = models.PositiveIntegerField()
    per13div = models.CharField(max_length = 50)
    per13 = models.CharField(max_length = 50)
    per30 = models.CharField(max_length = 50)
    countChild = models.CharField(max_length=2)
    checkChild = models.CharField(max_length = 50)
    checkInv = models.CharField(max_length = 50)
    dateStart = models.DateTimeField()
    result = models.CharField(max_length = 50)

    def __str__(self):
        return self.IDuser.username