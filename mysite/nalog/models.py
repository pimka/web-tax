from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)

class UserResults(models.Model):
    #IDuser = models.OneToOneField(User)
    IDuser = models.ForeignKey('auth.User')
    number = models.PositiveIntegerField(default=0)
    per13div = models.BooleanField(default=False)
    per13 = models.BooleanField(default=True)
    per30 = models.BooleanField(default=False)
    countChild = models.CharField(default='2', max_length=2)
    checkChild = models.BooleanField(default=False)
    checkInv = models.BooleanField(default=False)
    dateStart = models.DateTimeField(default=timezone.now())
    result = models.CharField(max_length = 50)

    def __str__(self):
        return self.IDuser.username