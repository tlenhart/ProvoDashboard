from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from Dashboard.models import Safety  # ,Civic, Government

# See https://django-tastypie.readthedocs.org/en/latest/interacting.html for info about interacting with the api.


class SafetyResource(ModelResource):
    class Meta:
        queryset = Safety.objects.all()
        resource_name = 'safety'

"""
class EconomicResource(ModelResource):
    class Meta:
        queryset = Economic.objects.all()
        resource_name = 'economic'
        filtering = {
            'category': ALL,
            'month': ALL,
            'year': ALL,
        }


            Call /api/economic/?year=2014 to filter objects by the year 2014.
            To make a column filterable, it must be added to the filtering object above.



class CivicResource(ModelResource):
    class Meta:
        queryset = Community.objects.all()  # Needs to change to Civic when the models are updated.
        resource_name = 'civic'


class GovernmentResource(ModelResource):
    class Meta:
        queryset = RecreationCultural.objects.all()  # Needs to change to Government when the models are updated.
        resource_name = 'government'
"""

