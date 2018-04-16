# coding=utf-8
"""Curriculum form."""

from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Field,
    Submit,
)

from modeltranslation.forms import TranslationModelForm

from lesson.models.curriculum import Curriculum


class CurriculumForm(TranslationModelForm):
    """Form for creating curriculum."""

    class Meta:
        model = Curriculum
        fields = (
            'title',
            'competency'
        )

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project')
        self.user = kwargs.pop('user')
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Project {}: curriculum details').format(self.project),
                Field('title', css_class='form_control'),
                Field('competency', css_class='form_control'),

                css_id='project-form'
            )
        )

        self.helper.layout = layout
        self.helper.html5_required = False

        super(CurriculumForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super(CurriculumForm, self).save(commit=False)
        instance.project = self.project
        instance.owner = self.user
        instance.save()
        return instance
