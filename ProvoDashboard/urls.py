from django.conf.urls import patterns, include, url
from django.contrib import admin
from Dashboard import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProvoDashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Dashboard.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
)
