from tastypie.resources import ModelResource
from Dashboard.models import Community, RecreationCultural, Economic, Safety  # ,Civic, Government


class SafetyResource(ModelResource):
    class Meta:
        queryset = Safety.objects.all()
        resource_name = 'safety'


class EconomicResource(ModelResource):
    class Meta:
        queryset = Economic.objects.all()
        resource_name = 'economic'


class CivicResource(ModelResource):
    class Meta:
        queryset = Community.objects.all()
        resource_name = 'civic'


class GovernmentResource(ModelResource):
    class Meta:
        queryset = RecreationCultural.objects.all()
        resource_name = 'government'


