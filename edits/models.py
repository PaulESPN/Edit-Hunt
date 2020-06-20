from django.db import models

# Create your models here.
class Edit(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    votecounter = models.IntegerField()

    def __str__(self):
        return self.title
