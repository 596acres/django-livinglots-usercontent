from django.views.generic import CreateView

from braces.views import FormValidMessageMixin

from livinglots_genericviews import AddGenericMixin


class AddContentView(FormValidMessageMixin, AddGenericMixin, CreateView):

    def _get_content_name(self):
        return self.form_class._meta.model._meta.object_name

    def get_form_valid_message(self):
        return '%s added successfully.' % self._get_content_name()

    def get_success_url(self):
        return self.get_content_object().get_absolute_url()

    def get_template_names(self):
        return [
            'livinglots/content/add_%s.html' % self._get_content_name().lower(),
        ]

    def form_valid(self, form):
        """
        Save the content and notify participants who are following the target
        lot.
        """
        self.object = form.save()
        # TODO as signals?
        #notify_participants_new_obj(self.object)
        return super(AddContentView, self).form_valid(form)
