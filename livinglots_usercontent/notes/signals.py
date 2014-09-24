from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Note
from ..signals import add_inplace_action


@receiver(post_save, sender=Note, dispatch_uid='activity_stream.note')
def add_note_action(sender, instance=None, **kwargs):
    if not instance: return
    add_inplace_action(instance.added_by, 'wrote', instance=instance, **kwargs)
