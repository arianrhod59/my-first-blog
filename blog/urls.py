from django.conf.urls import url
from . import views	#az összes view-t importáljuk

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),	# itt egy post_list nevű viewt rendeltünk hozzá a ^$ URL-hez. Azaz azért az üres(^$) regex, mert ha valaki a 'http://127.0.0.1:8000/' címen lép be a weboldaladra. Utána ezzel tudja h a views.post_list a helyes lépés. Ezt keresse. name='post_list' az URL neve, amit a view azonosítására használunk.
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]