from django.views import generic
from django.shortcuts import render

from blog.models import ShortNews, Category


class AnasayfaView(generic.ListView):
    model = ShortNews


class KategoriView(generic.DetailView):
    def get_queryset(self):
        return Category.objects.all()


class HaberView(generic.DetailView):
    def get_queryset(self):
        return ShortNews.objects.filter(report_count=0)


class SSSView(generic.TemplateView):
    template_name = "blog/sss.html"