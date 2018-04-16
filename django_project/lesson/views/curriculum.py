# coding=utf-8
"""Curriculum views."""

from collections import OrderedDict

from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from braces.views import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin


from base.models.project import Project
from lesson.models.curriculum import Curriculum
from lesson.forms.curriculum import CurriculumForm
from lesson.models.worksheet import Worksheet

class CurriculumMixin(object):
    """Mixin class to provide standard settings for Curriculum."""

    model = Curriculum
    form_class = CurriculumForm


class CurriculumListView(CurriculumMixin, PaginationMixin, ListView):
    """List view for Section."""

    context_object_name = 'curricula'
    template_name = 'curriculum/list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Get the context data which is passed to a template.

        :param kwargs: Any arguments to pass to the superclass.
        :type kwargs: dict

        :returns: Context data which will be passed to the template.
        :rtype: dict
        """
        context = super(CurriculumListView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project, slug=self.kwargs.get('project_slug', None))
        # context['worksheets'] = OrderedDict()
        # for curriculum in context['curricula']:
        #     query_set = Worksheet.objects.filter(curriculum=curriculum)
        #     context['worksheets'][curriculum] = query_set

        # Permissions
        context['user_can_edit'] = False
        if self.request.user in context['project'].lesson_managers.all():
            context['user_can_edit'] = True

        if self.request.user == context['project'].owner:
            context['user_can_edit'] = True

        if self.request.user.is_staff:
            context['user_can_edit'] = True

        return context

    def get_queryset(self):
        """Get the queryset for this view.

        :returns: A queryset which is filtered to only show approved Version
        for this project.
        :rtype: QuerySet

        :raises: Http404
        """
        section_qs = Curriculum.objects.all()
        project_slug = self.kwargs.get('project_slug', None)
        if project_slug:
            project = get_object_or_404(Project, slug=project_slug)
            return section_qs.filter(project=project)
        else:
            raise Http404('Sorry! We could not find your section!')


class CurriculumCreateView(LoginRequiredMixin, CurriculumMixin, CreateView):
    """Create view for Curriculum."""

    context_object_name = 'curriculum'
    template_name = 'create.html'
    creation_label = _('Add curriculum')

    def get_success_url(self):
        """Define the redirect URL

        After successful creation of the object, the User will be redirected
        to the unapproved Version list page for the object's parent Project

        :returns: URL
        :rtype: HttpResponse
        """
        url = '{url}#{anchor}'.format(
            url=reverse(
                'curriculum-list',
                kwargs={'project_slug': self.object.project.slug}),
            anchor=self.object.slug
        )
        return url

    def get_form_kwargs(self):
        """Get keyword arguments from form.

        :returns keyword argument from the form
        :rtype dict
        """
        kwargs = super(CurriculumCreateView, self).get_form_kwargs()
        project_slug = self.kwargs['project_slug']
        kwargs['project'] = get_object_or_404(Project, slug=project_slug)
        kwargs.update({'user': self.request.user})
        return kwargs