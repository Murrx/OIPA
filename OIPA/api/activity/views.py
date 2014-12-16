import django_filters
from rest_framework import filters
from rest_framework import generics
import iati
from api.activity import serializers
import api.generics


class ActivityFilter(django_filters.FilterSet):
    min_budget = django_filters.NumberFilter(
        name='total_budget', lookup_type='gte')
    reporting_organisation = django_filters.CharFilter(
        name='reporting_organisation__code',
        lookup_type='exact'
    )
    participating_organisations = django_filters.CharFilter(
        name='participating_organisations__organisation__code',
        lookup_type='in'
    )
    id = django_filters.Filter(
        name='id',
        lookup_type='in'
    )

    class Meta:
        model = iati.models.Activity
        fields = [
            'id',
            'total_budget',
            'min_budget',
            'reporting_organisation',
            'participating_organisations'
        ]


class ActivityList(api.generics.DynamicListAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ActivityFilter
    queryset = iati.models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    fields = [
        'url',
        'id',
        'title',
        'total_budget',
        'participating_organisations'
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
