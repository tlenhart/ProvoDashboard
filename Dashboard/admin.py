from django.contrib import admin
# Register your models here.
from .models import CivicHealth, EconomicHealth, GovernmentPerformance, SubCategories, PublicSafety

# The models need to change to Safety, Economic, Civic, and Government
admin.site.register(CivicHealth)
admin.site.register(EconomicHealth)
admin.site.register(GovernmentPerformance)
admin.site.register(SubCategories)
admin.site.register(PublicSafety)


