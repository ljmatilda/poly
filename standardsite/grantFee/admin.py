from django.contrib import admin

from .models import GrantFeePreCon, GrantFeeDocument

# Register your models here.
@admin.register(GrantFeePreCon)
class GrantFeePreConAdmin(admin.ModelAdmin):
	list_display = ('item_text', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(GrantFeeDocument)
class GrantFeeDocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')
