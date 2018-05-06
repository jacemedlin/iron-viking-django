from django.contrib import admin

# Register your models here.

from .models import Ambassador

class AmbassadorAdmin(admin.ModelAdmin):
	fieldsets = [
			('Ambassador Info', {'fields': ['name', 'about', 'berserker_or_shieldmaiden', 'image']}),
			(None, {'fields':['is_featured']}),
			('Ambassador Duration', {'fields':['ambassador_start', 'ambassador_end']})
	]
	
admin.site.register(Ambassador, AmbassadorAdmin)