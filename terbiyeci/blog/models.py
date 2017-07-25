import datetime
from django.db import models


class ShortNews(models.Model):
    title = models.CharField(max_length=200)
    source = models.URLField()
    created = models.DateTimeField(default=datetime.datetime.now)
    featured_for = models.DateTimeField(default=None, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    score = models.SmallIntegerField()
    report_count = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField("Category")


class Category(models.Model):
    name = models.CharField(max_length=50)
