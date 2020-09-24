from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Edit(models.Model):
    title = models.CharField(max_length=200)
    video =  EmbedVideoField()
    pub_date = models.DateField()
    votecounter = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) #User that submits video

    def pubdatepretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title


class Vote(models.Model):
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    edit = models.ForeignKey(Edit, on_delete=models.CASCADE)
