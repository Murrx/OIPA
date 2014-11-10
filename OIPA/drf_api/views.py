import geodata.models
import iati.models
import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'cities': reverse('city-list', request=request, format=format),
        'regions': reverse('region-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
    })

class CityList(generics.ListAPIView):
    queryset = geodata.models.City.objects.all()
    serializer_class = serializers.CityListSerializer


class CityDetail(generics.RetrieveAPIView):
    queryset = geodata.models.City.objects.all()
    serializer_class = serializers.CityDetailSerializer


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
        region = geodata.models.Region(pk=pk)
        return Response(country.name for country in region.country_set.all())


class RegionRelatedActivities(APIView):

    def get(self, request, pk):
        region = geodata.models.Region(pk=pk)
        return Response(activity.__unicode__() for activity in region.related_activities.all())