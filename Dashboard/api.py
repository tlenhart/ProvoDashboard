from tastypie.resources import ModelResource
from Dashboard.models import Transportation

class TransportationResource(ModelResource):
    class Meta:
        queryset = Transportation.objects.all()
        resource_name = 'transportation'
