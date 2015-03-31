from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from Dashboard.models import CivicHealth, EconomicHealth, GovernmentPerformance, SubCategories, PublicSafety

# See https://django-tastypie.readthedocs.org/en/latest/interacting.html for info about interacting with the api.

# Not callable directly with a url as it is not in urls.py
class CategoryResource(ModelResource):
    class Meta:
        queryset = SubCategories.objects.filter(visible=True)
        resource_name = 'category'
        filtering = {
            'description': ALL,
            'sub_category': ALL,
        }

class CivicResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = CivicHealth.objects.all()
        resource_name = 'civic'
        allowed_methods = ['get']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'month': ALL,
            'year': ALL,
        }

class EconomicResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = EconomicHealth.objects.all()
        resource_name = 'economic'
        allowed_methods = ['get']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'month': ALL,
            'year': ALL,
        }

class GovernmentResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = GovernmentPerformance.objects.all()
        resource_name = 'government'
        allowed_methods = ['get']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'month': ALL,
            'year': ALL,
        }


class SafetyResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)

    class Meta:
        queryset = PublicSafety.objects.all()
        resource_name = 'safety'
        allowed_methods = ['get']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'month': ALL,
            'year': ALL,
        }

        # To filter on an individual subcategory call (For example Violent Crimes):
        #   /api/safety/?category__sub_category=Violent%20Crimes


# class SafetyResource(ModelResource):
#     class Meta:
#         queryset = Safety.objects.all()
#         resource_name = 'safety'

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

