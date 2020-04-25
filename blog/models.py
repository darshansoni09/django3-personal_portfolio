from django.db import models

class Blog(models.Model):

    blogTitle = models.CharField(max_length = 100)
    blogDescription = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.blogTitle
