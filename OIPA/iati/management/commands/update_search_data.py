from django.core.management.base import BaseCommand
from iati import models


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for activity in models.Activity.objects.all():
            self.add_activity_search_data(activity)
        


    def add_activity_search_data(self, activity):
        
        search_data = models.ActivitySearchData(activity = activity)

        search_data.search_identifier = activity.iati_identifier
        for title in activity.title_set.all():
            search_data.search_title = u'{orig_title} {add_title} '.format(
                orig_title=search_data.search_title or '',
                add_title=title.title or ''
            )

        for description in activity.description_set.all():
            search_data.search_description = u'{orig_description} {add_description} '.format(
                orig_description=search_data.search_description or '',
                add_description=description.description or ''
            )

        for country in activity.recipient_country.all():
            search_data.search_country_name = u'{orig_country_name} {add_country_name} '.format(
                orig_country_name=search_data.search_country_name or '',
                add_country_name=country.name or ''
            )

        for region in activity.recipient_region.all():
            search_data.search_region_name = u'{orig_region_name} {add_region_name} '.format(
                orig_region_name=search_data.search_region_name or '',
                add_region_name=region.name or ''
            )

        for sector in activity.sector.all():
            search_data.search_sector_name = u'{orig_sector_name} {add_sector_name} '.format(
                orig_sector_name=search_data.search_sector_name or '',
                add_sector_name=sector.name or ''
            )

        for organisation in activity.participating_organisations.all():
            search_data.search_participating_organisation_name = u'{orig_organisation_name} {add_organisation_name} '.format(
                orig_organisation_name=search_data.search_participating_organisation_name or '',
                add_organisation_name=organisation.name or ''
            )

        if not activity.reporting_organisation is None:
            search_data.search_reporting_organisation_name = u'{add_organisation_name}'.format(
                add_organisation_name=activity.reporting_organisation.name or ''
            )

        for document in activity.documentlink_set.all():
            search_data.search_documentlink_title = u'{orig_documentlink_title} {add_documentlink_title} '.format(
                orig_documentlink_title=search_data.search_documentlink_title or '',
                add_documentlink_title=document.title or ''
            )

        search_data.save()
