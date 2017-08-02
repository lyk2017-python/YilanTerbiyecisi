from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.db.models import F
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CategoriedNewsForm, ContactForm, CustomUserCreationForm
from blog.models import ShortNews, Category

def like(request):
    id = request.POST.get("id", default=None)
    like = request.POST.get("like")
    obj = get_object_or_404(ShortNews, id=int(id))
    if like == "true":
        obj.score = F("score") + 1
        obj.save(update_fields=["score"])
    elif like == "false":
        obj.score = F("score") - 1
        obj.save(update_fields=["score"])
    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"like": obj.score, "id": id})


class LoginCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class AnasayfaView(generic.ListView):
    queryset = ShortNews.objects.filter(hidden=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = Category.objects.all()
        return context

class HaberCreateView(LoginCreateView):
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

    @method_decorator(login_required)
    def post(self, request, *a, **kw):
        return super().post(request, *a, **kw)

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
        context["news_list"] = context["object"].shortnews_set.filter(hidden=False)
        return context

class HaberView(generic.DetailView):
    def get_queryset(self):
        return ShortNews.objects.filter(hidden=False)


class SSSView(generic.TemplateView):
    template_name = "blog/sss.html"


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "blog/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
            "YilanTerbiyecisi ContactForm : {}".format(data["title"]),
            ("Sistemden size gelen bir bildirim var\n"
             "---\n"
             "{}\n"
             "---\n"
             "eposta={}\n"
             "ip={}").format(data["body"], data["email"], self.request.META["REMOTE_ADDR"]),
            settings.DEFAULT_FROM_EMAIL,
            ["cediddi@yilanterbiyecisi.com"]
        )
        return super().form_valid(form)


class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "blog/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
