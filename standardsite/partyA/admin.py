from django.contrib import admin

from .models import PartyAPreCon, PartyADocument

# Register your models here.
@admin.register(PartyAPreCon)
class PartyAPreConAdmin(admin.ModelAdmin):
	list_display = ('item_text', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(PartyADocument)
class PartyADocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')
