# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/$', include('blog.urls')),

    url(r'^loadingdiagram/processcalculation/$',views.process_calculation,name='processcalculation'),
    url(r'^loadingdiagram/calculate/$',views.calculate),
    url(r'^',views.process_calculation),
    
]