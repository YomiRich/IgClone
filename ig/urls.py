from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.photo_of_day,name = 'photoToday'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.search_by_location,name ='locations')
    

]
