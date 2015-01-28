from tastypie.resources import ModelResource
from Dashboard.models import Community, RecreationCultural, Economic, Environment, Transportation, Safety


class CommunityResource(ModelResource):
    class Meta:
        queryset = Community.objects.all()
        resource_name = 'community'


class RecreationCulturalResource(ModelResource):
    class Meta:
        queryset = RecreationCultural.objects.all()
        resource_name = 'recreationcultural'


class EconomicResource(ModelResource):
    class Meta:
        queryset = Economic.objects.all()
        resource_name = 'economic'


class EnvironmentResource(ModelResource):
    class Meta:
        queryset = Environment.objects.all()
        resource_name = 'environment'


class SafetyResource(ModelResource):
    class Meta:
        queryset = Safety.objects.all()
        resource_name = 'safety'


class TransportationResource(ModelResource):
    class Meta:
        queryset = Transportation.objects.all()
        resource_name = 'transportation'
