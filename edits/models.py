from django.db import models
from django.contrib.auth.models import User


class Edit(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateField()
    votecounter = models.IntegerField(default=1)
    body = models.TextField()
    icon = models.ImageField(upload_to='images/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) #User that submits video

    def pubdatepretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
