"""TestApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^index$', views.test),
    # url(r'^test$', views.template_one),
    # url(r'^test1$', views.templ)
    # url(r'^$', views.hello),
    url(r'^$', views.articles),
    url(r'^articles/all/$', views.articles),
    url(r'^articles/(?P<art_id>[0-9]+)/$', views.article),
    url(r'^articles/addlike/(?P<art_id>[0-9]+)/$', views.addlike),
    url(r'^articles/addcomment/(?P<art_id>\d+)/$', views.addcomment),
]
