from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.author
