from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    email    = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    company  = models.ForeignKey('recruits.Company', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'users'