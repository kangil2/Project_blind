from django.db import models

from core.models import TimeStampModel

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'categories'

class Company(models.Model):
    name     = models.CharField(max_length=50)
    image    = models.ImageField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'companies'

class Recruit(TimeStampModel):
    subject   = models.CharField(max_length=50)
    body      = models.TextField()
    tag       = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)
    file      = models.FileField()
    company   = models.ForeignKey('Company', on_delete=models.CASCADE)
    image_url = models.ImageField(null=True, upload_to="media/recruits/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'recruits'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tags'
        
