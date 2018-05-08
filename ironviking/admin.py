# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.models import User

from newsletter.models import Subscription
from ambassadors.models import Ambassador

# Main Site
class IronVikingAdmin(AdminSite):
	AdminSite.site_header = "Iron Viking Admin"
	
iron_viking_admin = IronVikingAdmin(name = 'ironadmin')
	
# Ambassador Model
class AmbassadorAdmin(ModelAdmin):
	fieldsets = [
			('Ambassador Info', {'fields': ['name', 'about', 'berserker_or_shieldmaiden', 'image']}),
			(None, {'fields':['is_featured']}),
			('Ambassador Duration', {'fields':['ambassador_start', 'ambassador_end']})
	]
	

	

# Registering database forms to admin site
iron_viking_admin.register(Subscription)
iron_viking_admin.register(Ambassador, AmbassadorAdmin)
iron_viking_admin.register(User)