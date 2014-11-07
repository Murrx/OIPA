from django.conf.urls import patterns, url
from drf_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    url(r'^$', views.api_root),
    url(r'^activities/$', views.ActivityList.as_view(), name='activity-list'),
    url(r'^cities/$', views.CityList.as_view(), name='city-list'),
    url(r'^regions/$', views.RegionList.as_view(), name='region-list'),

    url(r'^activities/(?P<pk>[^@$&+,/:;=?]+)/$',
        views.ActivityDetail.as_view(), name='activity-detail'
    ),
    url(r'^regions/(?P<pk>[0-9]+)/$', views.RegionDetail.as_view(), name='region-detail'),
    url(r'^cities/(?P<pk>[0-9]+)/$', views.CityDetail.as_view(), name='city-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
