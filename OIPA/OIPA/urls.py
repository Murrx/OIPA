from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic.base import RedirectView
from api import docs_views


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/queue/', include('django_rq.urls')),
    url(r'^admin/task_queue/', include('task_queue.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api', include('api.urls')),
    url(r'^docs(?P<api_call>/api.*)', docs_views.activity_list, name='docs'),
    url(r'^$',
        RedirectView.as_view(url='/api', permanent=True),
        name='index')
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
