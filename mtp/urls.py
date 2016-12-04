from django.conf.urls import include, url
from django.contrib import admin
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth_views.login, {'template_name': 'index.html'}, name="index"),    
    url(r'^logout/$', auth_views.logout,{'template_name': 'logout.html'}, name='logout'),
    url(r'^core/', include('core.urls')),
]
