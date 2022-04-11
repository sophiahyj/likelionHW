from django.db import models

# Create your models here.
class Day(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title