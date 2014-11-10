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
    related_activity_count = serializers.HyperlinkedIdentityField(view_name='region-activity-count')
    countries_in_region = serializers.HyperlinkedIdentityField(view_name='countries-in-region')
    related_activities = serializers.HyperlinkedIdentityField(view_name='region-related-activities')
    parental_region = serializers.HyperlinkedRelatedField(view_name='region-detail')
    child_regions = serializers.HyperlinkedIdentityField(view_name='child-regions',)
    class Meta:
        model = geodata.models.Region
        fields = ('code', 'name', 'region_vocabulary', 'center_longlat', 'parental_region', 'countries_in_region', 'related_activity_count', 'related_activities', 'child_regions',)

    def transform_activity_count(self, obj, value):
        pass


class RegionActivityCountSerializer(serializers.Serializer):
    activity_count = serializers.CharField(read_only=True)
    class Meta:
        fields = ()


class ActivityListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='activity-detail')
    descriptions = serializers.SlugRelatedField(many=True, slug_field='description')
    titles = serializers.SlugRelatedField(many=True, slug_field='title')

    class Meta:
        model = iati.models.Activity
        fields = ('id','url' , 'url','iati_identifier', 'titles', 'descriptions')


class ActivityDetailSerializer(ActivityListSerializer):
    sector = serializers.SlugRelatedField(many=True, slug_field='name')
    class Meta:
        model = iati.models.Activity
        fields = ()


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = geodata.models.Country
        fields = ()


class CountryListSerializer(serializers.ModelSerializer):
    code = serializers.HyperlinkedIdentityField(view_name='country-detail')
    class Meta:
        model = geodata.models.Country
        fields =('code', 'name', )
