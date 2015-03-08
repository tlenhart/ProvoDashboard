from django.contrib import admin
# Register your models here.
from .models import CivicHealth, EconomicHealth, GovernmentPerformance, PublicSafety, SubCategories
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CivicResource(resources.ModelResource):
    class Meta:
        model = CivicHealth

class EconomicResource(resources.ModelResource):
    class Meta:
        model = EconomicHealth

class GovernmentResource(resources.ModelResource):
    class Meta:
        model = GovernmentPerformance

class PublicResource(resources.ModelResource):
    class Meta:
        model = PublicSafety

class CivicAdmin(ImportExportModelAdmin):
    resource_class = CivicResource
    list_display = ('category', 'month', 'year')

class EconomicAdmin(ImportExportModelAdmin):
    resource_class = EconomicResource

class GovernmentAdmin(ImportExportModelAdmin):
    resource_class = GovernmentResource

class PublicAdmin(ImportExportModelAdmin):
    resource_class = PublicResource

# The models need to change to Safety, Economic, Civic, and Government
admin.site.register(CivicHealth, CivicAdmin)
admin.site.register(EconomicHealth, EconomicAdmin)
admin.site.register(GovernmentPerformance, GovernmentAdmin)
admin.site.register(PublicSafety, PublicAdmin)
admin.site.register(SubCategories)


