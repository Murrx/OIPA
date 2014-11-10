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
    url(r'^activities/(?P<pk>[^@$&+,/:;=?]+)/recipient-countries', views.RecipientCountries.as_view(), name='activity-recipient-countries'),

    url(r'^regions/(?P<pk>[0-9]+)/$', views.RegionDetail.as_view(), name='region-detail'),
    url(r'^cities/(?P<pk>[0-9]+)/$', views.CityDetail.as_view(), name='city-detail'),
    url(r'^regions/(?P<pk>[0-9]+)/countries-in-region', views.CountriesInRegion.as_view(), name='countries-in-region'),
    url(r'^regions/(?P<pk>[0-9]+)/activity-count', views.RegionActivityCount.as_view(), name='region-activity-count'),
    url(r'^regions/(?P<pk>[0-9]+)/related-activities', views.RegionRelatedActivities.as_view(), name='region-related-activities'),
    url(r'^regions/(?P<pk>[0-9]+)/child-regions', views.ChildRegionList.as_view(), name='child-regions'),

    url(r'^countries/$', views.CountryList.as_view(), name='country-list'),
    url(r'^countries/(?P<pk>[a-zA-z]+)/$', views.CountryDetail.as_view(), name='country-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
