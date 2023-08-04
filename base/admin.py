from django.contrib import admin

from .models import *


class AddContactAdmin(admin.StackedInline):
	model = MainContact
	
class MainAdmin(admin.ModelAdmin):
	inlines = [AddContactAdmin]

class AddAboutDetailed(admin.StackedInline):
	model=AboutDetailed

class AboutAdmin(admin.ModelAdmin):
	inlines=[AddAboutDetailed]
        
admin.site.register(Service)
admin.site.register(Slider)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(OpeningHours)
admin.site.register(Main, MainAdmin)
admin.site.register(MainContact)
admin.site.register(SocialMedia)
admin.site.register(BackgroundImage)
admin.site.register(Apply)
admin.site.register(Subscribe)
admin.site.register(About, AboutAdmin)
admin.site.register(AboutDetailed)
admin.site.register(ConsultingService)
admin.site.register(AboutApply)
admin.site.register(Map)
admin.site.register(Additional)
admin.site.register(HomeImage)
admin.site.register(HomeServiceDetail)