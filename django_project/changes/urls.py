# coding=utf-8
"""Urls for changelog application."""
from django.conf.urls import patterns, url
from django.conf import settings

from views import (
    # Category
    CategoryDetailView,
    CategoryDeleteView,
    CategoryCreateView,
    CategoryListView,
    JSONCategoryListView,
    CategoryUpdateView,
    PendingCategoryListView,
    ApproveCategoryView,
    # Version
    VersionMarkdownView,
    VersionDetailView,
    VersionThumbnailView,
    VersionDeleteView,
    VersionCreateView,
    VersionListView,
    VersionUpdateView,
    PendingVersionListView,
    ApproveVersionView,
    VersionDownload,
    # Entry
    EntryDetailView,
    EntryDeleteView,
    EntryCreateView,
    EntryListView,
    EntryUpdateView,
    PendingEntryListView,
    ApproveEntryView)

urlpatterns = patterns(
    '',
    # Category management

    # This view is only accessible via ajax
    url(regex='^json-category/list/(?P<version>\d+)/$',
        view=JSONCategoryListView.as_view(),
        name='json-category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/pending-category/list/$',
        view=PendingCategoryListView.as_view(),
        name='pending-category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/approve-category/(?P<project_slug>[\w-]+)/$',
        view=ApproveCategoryView.as_view(),
        name='category-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/category/list/$',
        view=CategoryListView.as_view(),
        name='category-list'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<category_slug>[\w-]+)/$',
        view=CategoryDetailView.as_view(),
        name='category-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<category_slug>[\w-]+)/delete/$',
        view=CategoryDeleteView.as_view(),
        name='category-delete'),
    url(regex='^category/create/$',
        view=CategoryCreateView.as_view(),
        name='category-create'),
    url(regex='^(?P<project_slug>[\w-]+)/category/(?P<category_slug>[\w-]+)/update/$',
        view=CategoryUpdateView.as_view(),
        name='category-update'),

    # Version management
    url(regex='^(?P<project_slug>[\w-]+)/pending-versions/list/$',
        view=PendingVersionListView.as_view(),
        name='pending-version-list'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/approve/$',
        view=ApproveVersionView.as_view(),
        name='version-approve'),
    url(regex='^(?P<project_version_slug>[\w-]+)/version/list/$',
        view=VersionListView.as_view(),
        name='version-list'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/markdown/$',
        view=VersionMarkdownView.as_view(),
        name='version-markdown'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/$',
        view=VersionDetailView.as_view(),
        name='version-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/thumbs/$',
        view=VersionThumbnailView.as_view(),
        name='version-thumbs'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/delete/$',
        view=VersionDeleteView.as_view(),
        name='version-delete'),
    url(regex='^version/create/$',
        view=VersionCreateView.as_view(),
        name='version-create'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/update/$',
        view=VersionUpdateView.as_view(),
        name='version-update'),
    url(regex='^(?P<project_slug>[\w-]+)/version/(?P<version_slug>[\w-]+)/download/$',
        view=VersionDownload.as_view(),
        name='version-download'),

    # Changelog entry management
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/'
              'pending-entry/list/$',
        view=PendingEntryListView.as_view(),
        name='pending-entry-list'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/entry/'
              '(?P<slug>[\w-]+)/approve/$',
        view=ApproveEntryView.as_view(),
        name='entry-approve'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/entry/list/$',
        view=EntryListView.as_view(),
        name='entry-list'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/entry'
              '/(?P<slug>[\w-]+)/$',
        view=EntryDetailView.as_view(),
        name='entry-detail'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/entry/'
              '(?P<slug>[\w-]+)/delete/$',
        view=EntryDeleteView.as_view(),
        name='entry-delete'),
    url(regex='^entry/create/$',
        view=EntryCreateView.as_view(),
        name='entry-create'),
    url(regex='^(?P<project_slug>[\w-]+)/(?P<version_slug>[\w-]+)/entry/'
              '(?P<slug>[\w-]+)/update/$',
        view=EntryUpdateView.as_view(),
        name='entry-update'),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
