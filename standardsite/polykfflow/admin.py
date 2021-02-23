from django.contrib import admin

from .models import PreSellCertPreCon, Document

# Register your models here.
@admin.register(PreSellCertPreCon)
class PreSellCertPreConAdmin(admin.ModelAdmin):
	list_display = ('id', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')