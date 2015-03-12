from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import ContentMixin


class Note(ContentMixin, models.Model):
    text = models.TextField(_('text'))

    def __unicode__(self):
        return '%d' % self.pk
