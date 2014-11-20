from rest_framework import serializers
import iati


class ActivityDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='activity-detail')

    activitypolicymarker_set = serializers.RelatedField(many=True)
    activityrecipientcountry_set = serializers.RelatedField(many=True)
    activityrecipientregion_set = serializers.RelatedField(many=True)
    activitysector_set = serializers.RelatedField(many=True)
    activitywebsite_set = serializers.RelatedField(many=True)
    budget_set = serializers.RelatedField(many=True)
    condition_set = serializers.RelatedField(many=True)
    contactinfo_set = serializers.RelatedField(many=True)
    countrybudgetitem_set = serializers.RelatedField(many=True)
    crsadd_set = serializers.RelatedField(many=True)
    current_activity = serializers.RelatedField(many=True)
    description_set = serializers.RelatedField(many=True)
    documentlink_set = serializers.RelatedField(many=True)
    ffs_set = serializers.RelatedField(many=True)
    location_set = serializers.RelatedField(many=True)
    otheridentifier_set = serializers.RelatedField(many=True)
    participating_organisations = serializers.RelatedField(many=True)
    planneddisbursement_set = serializers.RelatedField(many=True)
    result_set = serializers.RelatedField(many=True)
    title_set = serializers.RelatedField(many=True)
    transaction_set = serializers.RelatedField(many=True)

    class Meta:
        model = iati.models.Activity
        fields = (
            # Normal data
            'url',
            'id',
            'iati_identifier',
            'default_currency',
            'hierarchy',
            'last_updated_datetime',
            'linked_data_uri',
            'reporting_organisation',
            'secondary_publisher',
            'activity_status',
            'start_planned',
            'end_planned',
            'start_actual',
            'end_actual',
            'collaboration_type',
            'default_flow_type',
            'default_aid_type',
            'default_finance_type',
            'default_tied_status',
            'xml_source_ref',
            'total_budget_currency',
            'total_budget',
            'capital_spend',
            'scope',
            'iati_standard_version',

            # Linked data
            'participating_organisation',
            'policy_marker',
            'sector',
            'recipient_country',
            'recipient_region',

            # Reverse linked data
            'activitypolicymarker_set',
            'activityrecipientcountry_set',
            'activityrecipientregion_set',
            'activitysector_set',
            'activitywebsite_set',
            'budget_set',
            'condition_set',
            'contactinfo_set',
            'countrybudgetitem_set',
            'crsadd_set',
            'current_activity',
            'description_set',
            'documentlink_set',
            'ffs_set',
            'location_set',
            'otheridentifier_set',
            'participating_organisations',
            'planneddisbursement_set',
            'result_set',
            'title_set',
            'transaction_set',
        )


class ActivityListSerializer(ActivityDetailSerializer):
    class Meta:
        model = iati.models.Activity
        fields = ('id', 'url', 'title_set')