from django.db import models
from django.contrib.auth.models import User

class UserResults(models.Model):
    IDuser = models.OneToOneField(User)

    dateStart = models.DateTimeField()
    result = models.BigIntegerField()

    def __str__(self):
        return self.IDuser.username