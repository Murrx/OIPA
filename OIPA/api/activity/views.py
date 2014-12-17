from rest_framework import filters
from rest_framework import generics
import iati
from api.activity import serializers
import api.generics


class CustomFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        print dir(request)
        print request.QUERY_PARAMS.get('id', '').split(',')
        return queryset.filter(id=1)


class ActivityList(api.generics.DynamicListAPIView):
    queryset = iati.models.Activity.objects.all()
    filter_backends = (CustomFilter,)
    filter_class = CustomFilter  # Not sure if this is needed
    serializer_class = serializers.ActivitySerializer
    fields = [
        'url',
        'id',
        'title',
        'total_budget',
    ]


class ActivityDetail(api.generics.DynamicRetrieveAPIView):
    queryset = iati.models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivitySectors(generics.ListAPIView):
    serializer_class = serializers.ActivitySectorSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return iati.models.Activity(pk=pk).activitysector_set.all()


class ActivityParticipatingOrganisations(generics.ListAPIView):
    serializer_class = serializers.ParticipatingOrganisationSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return iati.models.Activity(pk=pk).participating_organisations.all()


class ActivityRecipientCountry(generics.ListAPIView):
    serializer_class = serializers.RecipientCountrySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return iati.models.Activity(pk=pk).activityrecipientcountry_set.all()
