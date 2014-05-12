from django.contrib import admin


class BaseUserContentAdmin(admin.ModelAdmin):
    list_filter = ('added',)
    readonly_fields = ('added', 'content_type', 'object_id',)
