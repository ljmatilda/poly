from django.contrib import admin

from .models import LandGrantContractPreCon, LandGrantContractDocument

# Register your models here.
@admin.register(LandGrantContractPreCon)
class LandGrantContractPreConAdmin(admin.ModelAdmin):
	list_display = ('item_text', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(LandGrantContractDocument)
class LandGrantContractDocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')
