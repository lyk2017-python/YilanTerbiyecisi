import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class ShortNews(models.Model):
    title = models.CharField(max_length=200)
    source = models.URLField()
    created = models.DateTimeField(default=datetime.datetime.now)
    featured_for = models.DateTimeField(default=None, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    score = models.SmallIntegerField(default=0)
    report_count = models.PositiveSmallIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    categories = models.ManyToManyField("Category")
    parent_news = models.ForeignKey("self", blank=True, null=True, related_name="children_news")
    slug = models.SlugField(unique=True, blank=True, null=False)

    def __str__(self):
        return "#{id} {title}".format(id=self.id, title=self.title)

    class Meta:
        get_latest_by = "created"
        ordering = ['title']
        verbose_name = "Short News"
        verbose_name_plural = "Short News"


class Category(models.Model):
    """Class for news categories"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=False)

    def __str__(self):
        return "#{id} {name}".format(id=self.id, name=self.name)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=ShortNews)
def slug_belirle(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        elif hasattr(sender, "title"):
            instance.slug = slugify(instance.title)
        else:
            raise AttributeError("Slug belirlemek için name ya da title gerek")
    return instance

@receiver(pre_save, sender=ShortNews)
def auto_hidden(sender, instance, *args, **kwargs):
    if instance.report_count >= 10:
        instance.hidden = True
    return instance

