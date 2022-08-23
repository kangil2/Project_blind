from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at  = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True