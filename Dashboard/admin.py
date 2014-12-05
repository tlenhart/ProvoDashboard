from django.contrib import admin
# Register your models here.
from .models import SampleData, Community, RecreationCultural, Economic, Environment, Safety, Transportation


admin.site.register(SampleData)
admin.site.register(Community)
admin.site.register(RecreationCultural)
admin.site.register(Economic)
admin.site.register(Environment)
admin.site.register(Safety)
admin.site.register(Transportation)