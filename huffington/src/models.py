from django.db import models


class Article(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=264, blank=False)
