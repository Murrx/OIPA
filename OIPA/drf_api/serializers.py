import geodata.models
import iati.models
from rest_framework import serializers
from rest_framework.reverse import reverse


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.City
        fields = ('id', 'geoname_id', 'name', 'ascii_name', 'alt_name',
            'namepar', 'country', 'location'
        )

        
class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.City
        fields = ('id', 'name', 'country', 'location')


class RegionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'url', 'name')


class RegionDetailSerializer(serializers.ModelSerializer):
    activity_count = serializers.HyperlinkedIdentityField(view_name='region-activity-count')
    countries_in_region = serializers.HyperlinkedIdentityField(view_name='countries-in-region')
    #related_activities = serializers.HyperlinkedRelatedField(many=True, view_name='activity-detail', read_only=True)
    related_activities = serializers.HyperlinkedIdentityField(view_name='region-related-activities')
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'name', 'region_vocabulary', 'parental_region', 'center_longlat', 'countries_in_region', 'activity_count', 'related_activities')


class RegionActivityCountSerializer(serializers.Serializer):
    activity_count = serializers.CharField(read_only=True)
    class Meta:
        fields = ()


class ActivityListSerializer(serializers.ModelSerializer):
    descriptions = serializers.SlugRelatedField(many=True, slug_field='description')
    titles = serializers.SlugRelatedField(many=True, slug_field='title')

    class Meta:
        model = iati.models.Activity
        fields = ('id','iati_identifier', 'titles', 'descriptions')


class ActivityDetailSerializer(ActivityListSerializer):
    sector = serializers.SlugRelatedField(many=True, slug_field='name')
    class Meta:
        model = iati.models.Activity
        fields = ()
