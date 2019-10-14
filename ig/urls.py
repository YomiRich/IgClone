from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.photo_of_day,name = 'profileToday'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^profile/(\d+)',views.search_by_profile,name ='profiles')

]