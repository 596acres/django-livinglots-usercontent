from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_by_name', 'added',)
    list_filter = ('added',)
    readonly_fields = ('added', 'content_type', 'object_id',)
    search_fields = ('title', 'description', 'added_by_name',)


admin.site.register(File, FileAdmin)
