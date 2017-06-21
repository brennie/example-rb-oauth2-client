"""Client URLs."""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from example_client.client import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^accounts/profile/$', views.profile, name='user-profile'),
    url(r'^social/', include('social_django.urls')),
    url(r'^$', views.index, name='index'),
]
