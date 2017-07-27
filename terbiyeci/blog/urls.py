from django.conf.urls import url
from blog.views import AnasayfaView, KategoriView, HaberView, SSSView, HaberCreateView

urlpatterns = [
    url(r"^$", AnasayfaView.as_view(), name="home"),
    url(r"^yenihaber/$", HaberCreateView.as_view(), name="newnews"),
    url(r"^kategori/(?P<slug>[A-Za-z0-9\-]+)/$", KategoriView.as_view(), name="category_detail"),
    url(r"^detay/(?P<pk>\d+)/$", HaberView.as_view(), name="news_detail"),
    url(r"^sss/$", SSSView.as_view(), name="faq"),
]