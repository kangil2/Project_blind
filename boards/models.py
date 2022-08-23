from django.db import models

from core.models import TimeStampModel

class Topic(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'topics'

class TopicBoard(TimeStampModel):
    subject = models.CharField(max_length=50)
    like    = models.IntegerField()
    body    = models.TextField()
    image   = models.ImageField(null=True, upload_to="media/boards/%Y/%m/%d", blank=True)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    topic   = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'topicboards'

class ReviewBoard(TimeStampModel):
    evaluate = models.IntegerField()
    like     = models.IntegerField()
    subject  = models.CharField(max_length=30)
    body     = models.TextField()
    user     = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    company  = models.ForeignKey('recruits.Company', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviewboards'

class Comment(TimeStampModel):
    body       = models.CharField(max_length=100)
    like       = models.IntegerField()
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    topicboard = models.ForeignKey('TopicBoard', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

class Recomment(TimeStampModel):
    body    = models.CharField(max_length=100)
    like    = models.IntegerField()
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'recomments'