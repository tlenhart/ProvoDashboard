from django.contrib import admin
# Register your models here.
from .models import Community, RecreationCultural, Economic, Environment, Safety, Transportation

# The models need to change to Safety, Economic, Civic, and Government
admin.site.register(Community)
admin.site.register(RecreationCultural)
admin.site.register(Economic)
admin.site.register(Environment)
admin.site.register(Safety)
admin.site.register(Transportation)