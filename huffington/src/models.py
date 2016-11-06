from django.db import models


class Author(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=264, blank=False)


class ArticleOrComment(models.Model):
    author = models.ForeignKey(Author)
    date = models.DateField()
    parent = models.ForeignKey('self')
    is_article = models.BooleanField()


