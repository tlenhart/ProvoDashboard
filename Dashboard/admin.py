from django.contrib import admin
# Register your models here.
from .models import CivicHealth, EconomicHealth, GovernmentPerformance, PublicSafety, SubCategories

# The models need to change to Safety, Economic, Civic, and Government
admin.site.register(CivicHealth)
admin.site.register(EconomicHealth)
admin.site.register(GovernmentPerformance)
admin.site.register(PublicSafety)
admin.site.register(SubCategories)


