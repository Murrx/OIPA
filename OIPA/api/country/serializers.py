from rest_framework import serializers
import geodata
from api.generics.serializers import DynamicFieldsModelSerializer
from api.generics.serializers import DynamicFieldsSerializer
from api.region.serializers import RegionSerializer
from api.fields import JSONField
from api.activity.aggregation import AggregationsSerializer
from api.generics.serializers import FilteredListSerializer
from api.activity.filters import ActivityFilter


class CountrySerializer(DynamicFieldsModelSerializer):
    class ActivitiesSerializer(DynamicFieldsSerializer):
        url = serializers.HyperlinkedIdentityField(
            view_name='country-activities')
        aggregations = AggregationsSerializer(source='activity_set', fields=())

        class Meta:
            filter_class = ActivityFilter

    class BasicCitySerializer(serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='city-detail')

        class Meta:
            model = geodata.models.City
            fields = (
                'url',
                'id',
                'name'
            )

    url = serializers.HyperlinkedIdentityField(view_name='country-detail')
    region = RegionSerializer(fields=('url', 'code', 'name'))
    un_region = RegionSerializer(fields=('url', 'code', 'name'))
    unesco_region = RegionSerializer(fields=('url', 'code', 'name'))
    capital_city = BasicCitySerializer()
    location = JSONField(source='center_longlat.json')
    polygon = JSONField()
    activities = ActivitiesSerializer(source='*')
    indicators = serializers.HyperlinkedIdentityField(
        view_name='country-indicators')
    cities = serializers.HyperlinkedIdentityField(view_name='country-cities')

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = geodata.models.Country
        fields = (
            'url',
            'code',
            'numerical_code_un',
            'name',
            'alt_name',
            'language',
            'capital_city',
            'region',
            'un_region',
            'unesco_region',
            'dac_country_code',
            'iso3',
            'alpha3',
            'fips10',
            'data_source',
            'activities',
            'indicators',
            # 'adm1region_set',
            'cities',
            'location',
            'polygon',
        )
