from django.conf.urls import url
from blog.views import like, AnasayfaView, KategoriView, HaberView, SSSView, HaberCreateView, ContactFormView

urlpatterns = [
    url(r"^$", AnasayfaView.as_view(), name="home"),
    url(r"^yenihaber/$", HaberCreateView.as_view(), name="newnews"),
    url(r"^kategori/(?P<slug>[A-Za-z0-9\-]+)/$", KategoriView.as_view(), name="category_detail"),
    url(r"^detay/(?P<pk>\d+)/$", HaberView.as_view(), name="news_detail"),
    url(r"^iletisim/$", ContactFormView.as_view(), name="contact"),
    url(r"^sss/$", SSSView.as_view(), name="faq"),
    url(r"^api/like$", like, name="like_dislike"),
]