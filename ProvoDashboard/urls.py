from django.conf.urls import patterns, include, url
from Dashboard import *
from django.contrib import admin

# If the admin interface isn't working for you, delete the database, run manage.py syncdb, and set up the superuser.
# Then run:
#   manage.py makemigrations
#   manage.py migrate
# The last import statement in this file should be: from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProvoDashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Will need more urls for detailed graph pages. These need to be generated...

    url(r'^$', 'Dashboard.views.index', name='index'),
    url(r'^index', 'Dashboard.views.index'),
    url(r'^community', 'Dashboard.views.community', name='community'),
    url(r'^economic', 'Dashboard.views.economic', name='economic'),
    url(r'^environment', 'Dashboard.views.environment', name='environment'),
    url(r'^recreation', 'Dashboard.views.recreation', name='recreation'),
    url(r'^cultural', 'Dashboard.views.cultural', name='cultural'), # cultural and recreation go to the same page.
    url(r'^safety', 'Dashboard.views.safety', name='safety'),
    url(r'^transportation', 'Dashboard.views.transportation', name='transportation'),
    url(r'^admin/', include(admin.site.urls)),
)
