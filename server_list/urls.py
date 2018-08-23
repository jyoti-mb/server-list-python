from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^server/$', views.ServerList.as_view()),
    url(r'^server/(?P<pk>[0-9]+)/$', views.ServerDetail.as_view()),
]