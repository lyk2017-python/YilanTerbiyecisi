import datetime
from django.db import models


class ShortNews(models.Model):
    title = models.CharField(max_length=200)
    source = models.URLField()
    created = models.DateTimeField(default=datetime.datetime.now)
    featured_for = models.DateTimeField(default=None, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    score = models.SmallIntegerField(default=0)
    report_count = models.PositiveSmallIntegerField(default=0)
    categories = models.ManyToManyField("Category")
    def __str__(self):
        return "#{id} {title}".format(id=self.id, title=self.title)


class Category(models.Model):
    """Class for news categories"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "#{id} {name}".format(id=self.id, name=self.name)
