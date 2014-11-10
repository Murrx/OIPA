import geodata.models
import iati.models
import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from itertools import chain

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'cities': reverse('city-list', request=request, format=format),
        'regions': reverse('region-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'countries': reverse('country-list', request=request, format=format),
    })

class CityList(generics.ListAPIView):
    queryset = geodata.models.City.objects.all()
    serializer_class = serializers.CityListSerializer


class CityDetail(generics.RetrieveAPIView):
    queryset = geodata.models.City.objects.all()
    serializer_class = serializers.CityDetailSerializer


class CountryList(generics.ListAPIView):
    queryset = geodata.models.Country.objects.all()
    serializer_class = serializers.CountryListSerializer


class CountryDetail(generics.RetrieveAPIView):
    queryset = geodata.models.Country.objects.all()
    serializer_class = serializers.CountryDetailSerializer

class RegionList(generics.ListAPIView):
    queryset = geodata.models.Region.objects.all()
    serializer_class = serializers.RegionListSerializer


class RegionDetail(generics.RetrieveAPIView):
    queryset = geodata.models.Region.objects.all()
    serializer_class = serializers.RegionDetailSerializer


class RegionActivityCount(generics.RetrieveAPIView):
    serializer_class = serializers.RegionActivityCountSerializer

    def get(self, request, pk):
        activity_count = iati.models.Activity.objects.filter(recipient_region=pk).count()
        serializer = serializers.RegionActivityCountSerializer(data=activity_count)
        return Response({'activity_count': activity_count})


class ActivityList(generics.ListAPIView):
    queryset = iati.models.Activity.objects.all()
    serializer_class = serializers.ActivityListSerializer


class ActivityDetail(generics.RetrieveAPIView):
    queryset = iati.models.Activity.objects.all()
    serializer_class = serializers.ActivityDetailSerializer


class CountriesInRegion(APIView):

    def get(self, request, pk):
        data = {
            'countries': (reverse('country-detail', args=[country.code], request=request,) for country in self.get_countries(pk))
        }
        return Response(data)

    def get_countries(self, pk):
        region = geodata.models.Region(pk=pk)
        child_regions = region.region_set.all()
        countries = list (region.un_region.all())
        if child_regions.exists():
            pass
            for region in child_regions:
                countries += list(self.get_countries(region.pk))
        return countries


class RegionRelatedActivities(generics.ListAPIView):
    serializer_class = serializers.ActivityListSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return geodata.models.Region(pk=pk).related_activities.all()


class ChildRegionList(generics.ListAPIView):
    serializer_class = serializers.RegionListSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        region = geodata.models.Region(pk=pk)
        return list(region.region_set.all())
