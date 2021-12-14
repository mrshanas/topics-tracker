from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A class to create Topics"""

    title = models.CharField(max_length=250)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    """For entering entries"""

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    body = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body[:50]}..."
    class Meta:
        verbose_name_plural = 'entries'

    

