from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.photo_of_day,name = 'photoToday'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.search_by_location,name ='locations')
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)