from rest_framework import serializers
import geodata
import iati.models
from api.generics.serializers import DynamicFieldsModelSerializer
from api.fields import GeometryField
from api.activity.aggregation import AggregationsSerializer


class RegionVocabularySerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = iati.models.RegionVocabulary
        fields = ('code',)


class BasicRegionSerializer(DynamicFieldsModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='region-detail')
    code = serializers.CharField()
    region_vocabulary = RegionVocabularySerializer()

    class Meta:
        model = geodata.models.Region
        fields = (
            'url',
            'code',
            'name',
            'region_vocabulary'
        )


class RegionSerializer(DynamicFieldsModelSerializer):
    class ActivitiesSerializer(serializers.Serializer):
        url = serializers.HyperlinkedIdentityField(
            view_name='region-activities')
        aggregations = AggregationsSerializer(source='activity_set', fields=())

        class Meta:
            fields = (
                'activities',
                'aggregations')

    child_regions = BasicRegionSerializer(
        many=True, source='region_set', fields=('url', 'code', 'name'))
    parental_region = BasicRegionSerializer(fields=('url', 'code', 'name'))
    activities = ActivitiesSerializer(source='*')
    countries = serializers.HyperlinkedIdentityField(
        view_name='region-countries')
    location = GeometryField(source='center_longlat')

    class Meta:
        model = geodata.models.Region
        fields = (
            'url',
            'code',
            'name',
            'region_vocabulary',
            'parental_region',
            'countries',
            'location',
            'child_regions',
            'activities'
        )
