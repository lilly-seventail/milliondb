from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]