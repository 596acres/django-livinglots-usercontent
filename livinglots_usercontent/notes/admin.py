from django.contrib import admin

from ..admin import BaseUserContentAdmin
from .models import Note


class NoteAdmin(BaseUserContentAdmin):
    list_display = ('added_by_name', 'text', 'added',)
    search_fields = ('text', 'added_by_name',)


admin.site.register(Note, NoteAdmin)
