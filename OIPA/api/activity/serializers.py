from rest_framework import serializers
import iati


class ActivityDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='activity-detail')

    # Linked fields
    sectors = serializers.HyperlinkedIdentityField(
        view_name='activity-sectors')

    # Reverse linked fields
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
            # Normal fields
            'url',  # |x| iati: -
            'id',  # |x| iati: -
            'iati_identifier',  # |?| iati: iati-identifier
            'default_currency',  # |?| iati: default-currency
            'hierarchy',  # |v| iati: hierarchy
            'last_updated_datetime',  # |?| iati: last-updated-datetime
            'linked_data_uri',  # |?| iait: linked-data-uri
            'reporting_organisation',  # |x| iati: reporting-org
            'secondary_publisher',  # |x| iati: secondary-reporter
                                    # |x| property of reporting-org
            'activity_status',  # |v| iati: activity-status
            'start_planned',  # |x| iati: activity-date.start-planned
            'end_planned',  # |x| iati: activity-date.end-planned
            'start_actual',  # |x| iati: activity-date.start-actual
            'end_actual',  # |x| iati: activity-date.end-actual
            'collaboration_type',  # |?| iati: collaboration-type
            'default_flow_type',  # |?| iati: default-flow-type
            'default_aid_type',  # |?| iati: default-aid-type
            'default_finance_type',  # |?| iati: default-finance-type
            'default_tied_status',  # |?| iati: default-tied-status
            'xml_source_ref',  # |x| iati: -
            'total_budget_currency',  # |x| iati: -
            'total_budget',  # |x| iati: -
            'capital_spend',  # |?| iati: capital-spend
            'scope',  # |x| iati: activity-scope
            'iati_standard_version',  # |x| iati: -

            # Linked fields
            'participating_organisation',  # |x| iati: participaing-org
            'policy_marker',  # |?| iati: policy-marker
            'sectors',  # |?| iati: sector
            'recipient_country',  # |?| iati: recipient-country
            'recipient_region',  # |?| iati: recipient-region

            # Reverse linked fields
            'activitypolicymarker_set',  # |x| iati: policy-marker
            'activityrecipientcountry_set',  # |x| iati: recipient-country
            'activityrecipientregion_set',  # |x| iati: recipient-region
            'activitysector_set',  # |x| iati: sector
            'activitywebsite_set',  # |x| iati: contact-info.website
            'budget_set',  # |x| iati: budget
            'condition_set',  # |x| iati: conditions
            'contactinfo_set',  # |x| iati: contact-info
            'countrybudgetitem_set',  # |x| iati: country-budget-items
            'crsadd_set',  # |x| iati: crs-add
            'current_activity',  # |x| iati: related-activity
                                 # |x| rename: related_activities
            'description_set',  # |x| iati: description
            'documentlink_set',  # |x| iati: document-link
            'ffs_set',  # |x| iati: fss
                        # |x| name verry wrong
            'location_set',  # |x| iati: location
            'otheridentifier_set',  # |x| iati: other-identifier
            'participating_organisations',  # |x| iati: participating-org
            'planneddisbursement_set',  # |x| iati: planned-disbursement
            'result_set',  # |x| iati: result
            'title_set',  # |x| iati: title
            'transaction_set',  # |x| iati: transaction
        )


class ActivityListSerializer(ActivityDetailSerializer):
    class Meta:
        model = iati.models.Activity
        fields = ('id', 'url', 'title_set')


class ActivitySectorSerializer(serializers.ModelSerializer):
    activity = serializers.HyperlinkedRelatedField(view_name='activity-detail')
    sector = serializers.HyperlinkedRelatedField(view_name='sector-detail')

    class Meta:
        model = iati.models.ActivitySector
        fields = (
            'activity',
            'sector',
            'alt_sector_name',
            'vocabulary',
            'percentage',
        )
