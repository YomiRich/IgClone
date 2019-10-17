from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.photo_of_day,name = 'photoToday'),
    url(r'^search/$',views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.search_by_location,name ='locations'),
    url(r'^login/profile/',views.profile,name ='profile'),
    url(r'^login/edit_profile/',views.edit_profile,name ='edit_profile'),
    url(r'^signup/$',views.signup,name='signup')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)