from django.contrib import admin

from .models import LevelOneComPreCon, LevelOneComDocument

# Register your models here.
@admin.register(LevelOneComPreCon)
class LevelOneComPreConAdmin(admin.ModelAdmin):
	list_display = ('item_text', 'content_text', 'dock_apartment_txt', 'time_text', 'time_to_begin_text', 'description')

@admin.register(LevelOneComDocument)
class LevelOneComDocumentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_text', 'dock_apartment_txt', 'file', 'description')
