from django.conf.urls import patterns, include, url
from Dashboard import *
from django.contrib import admin
from Dashboard.api import CommunityResource, RecreationCulturalResource, EconomicResource, EnvironmentResource, SafetyResource, TransportationResource

community_resource = CommunityResource()
recreationcultural_resource = RecreationCulturalResource()
economic_resource = EconomicResource()
environment_resource = EnvironmentResource()
safety_resource = SafetyResource()
transportation_resource = TransportationResource()

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
    url(r'^civic', 'Dashboard.views.civic', name='civic'),
    url(r'^economic', 'Dashboard.views.economic', name='economic'),
    url(r'^government', 'Dashboard.views.government', name='government'), # cultural and recreation go to the same page.
    url(r'^safety', 'Dashboard.views.safety', name='safety'),
    (r'^api/', include(community_resource.urls)),
    (r'^api/', include(recreationcultural_resource.urls)),
    (r'^api/', include(economic_resource.urls)),
    (r'^api/', include(environment_resource.urls)),
    (r'^api/', include(safety_resource.urls)),
    (r'^api/', include(transportation_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
