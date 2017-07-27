from django.http import Http404
from django.views import generic
from django.shortcuts import render

from blog.forms import CategoriedNewsForm
from blog.models import ShortNews, Category

class AnasayfaView(generic.ListView):
    model = ShortNews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = Category.objects.all()
        return context

class HaberCreateView(generic.CreateView):
    model = ShortNews
    success_url = "/"
    fields = [
        "title",
        "source",
        "created",
        "featured_for",
        "image",
        "categories",
        "slug",
    ]


class KategoriView(generic.CreateView):
    form_class = CategoriedNewsForm
    template_name = "blog/category_create.html"
    success_url = "."

    def get_category(self):
        query = Category.objects.filter(slug=self.kwargs["slug"])
        if query.exists():
            return query.get()
        else:
            raise Http404("Category not found")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["categories"] = [self.get_category()]
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_category()
        return context

class HaberView(generic.DetailView):
    def get_queryset(self):
        return ShortNews.objects.filter(report_count=0)


class SSSView(generic.TemplateView):
    template_name = "blog/sss.html"