from django.conf.urls import url
from blog.views import AnasayfaView, KategoriView, HaberView, SSSView

urlpatterns = [
    url(r"^$", AnasayfaView, name="home"),
    url(r"^kategori/(?P<slug>[A-Za-z0-9\-]+)$", KategoriView, name="category_detail"),
    url(r"^detay/(?P<pk>\d+)-(?P<slug>[A-Za-z0-9\-]+)$", HaberView, name="news_detail"),
    url(r"^sss$", SSSView, name="faq"),
]