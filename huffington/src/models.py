from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=120)
    date = models.DateField()
    text = models.TextField()
    fb_graph_api_id = models.CharField(max_length=120)

