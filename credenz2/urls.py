"""credenz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rc import views

urlpatterns = [
    
    url(r'^$',views.home),
	url(r'^createuser$',views.createuser),
    url(r'^start', views.time_start),
	url(r'^login$',views.log_in),
	url(r'^login_page', views.login_page),
	url(r'^check',views.check),
    url(r'^ques_page',views.ques_page),
    url(r'^ques', views.ques),
    url(r'^start', views.time_start),
    url(r'^time', views.return_timezone),
    url(r'^logout',views.log_out),
    url(r'^result',views.result),
    url(r'^light_gone', views.add_time),
    url(r'^add_time', views.light_gone),
    url(r'^set_timezone',views.set_timezone),
	url(r'^admin_pisb/', include(admin.site.urls)),
]
