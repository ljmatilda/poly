from django.contrib import admin

from .models import ContractTaxPreCon, ContractTaxDocument

# Register your models here.
@admin.register(ContractTaxPreCon)
class ContractTaxPreConAdmin(admin.ModelAdmin):
	list_display = ('item_text', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(ContractTaxDocument)
class ContractTaxDocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')
