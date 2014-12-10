# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.CharField(max_length=150, serialize=False, primary_key=True)),
                ('iati_identifier', models.CharField(max_length=150)),
                ('hierarchy', models.SmallIntegerField(default=1, null=True, choices=[(1, 'Parent'), (2, 'Child')])),
                ('last_updated_datetime', models.CharField(default=None, max_length=100, null=True)),
                ('linked_data_uri', models.CharField(max_length=100, null=True, blank=True)),
                ('secondary_publisher', models.BooleanField(default=False)),
                ('start_planned', models.DateField(default=None, null=True, blank=True)),
                ('end_planned', models.DateField(default=None, null=True, blank=True)),
                ('start_actual', models.DateField(default=None, null=True, blank=True)),
                ('end_actual', models.DateField(default=None, null=True, blank=True)),
                ('xml_source_ref', models.CharField(max_length=200, null=True)),
                ('total_budget', models.DecimalField(default=None, null=True, max_digits=15, decimal_places=2, db_index=True)),
                ('capital_spend', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('iati_standard_version', models.CharField(default=None, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityDateType',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityParticipatingOrganisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=None, null=True)),
                ('activity', models.ForeignKey(related_name=b'participating_organisations', to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityPolicyMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alt_policy_marker', models.CharField(default=None, max_length=200, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityRecipientCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentage', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('country', models.ForeignKey(to='geodata.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityRecipientRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentage', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('region', models.ForeignKey(to='geodata.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityScope',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivitySearchData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_identifier', models.CharField(max_length=150, db_index=True)),
                ('search_description', models.TextField(max_length=80000)),
                ('search_title', models.TextField(max_length=80000)),
                ('search_country_name', models.TextField(max_length=80000)),
                ('search_region_name', models.TextField(max_length=80000)),
                ('search_sector_name', models.TextField(max_length=80000)),
                ('search_participating_organisation_name', models.TextField(max_length=80000)),
                ('search_reporting_organisation_name', models.TextField(max_length=80000)),
                ('search_documentlink_title', models.TextField(max_length=80000)),
                ('activity', models.OneToOneField(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivitySector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alt_sector_name', models.CharField(default=None, max_length=200, null=True)),
                ('percentage', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityWebsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=150)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AidType',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AidTypeCategory',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AidTypeFlag',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.CharField(default=None, max_length=50, null=True)),
                ('period_end', models.CharField(default=None, max_length=50, null=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('value_date', models.DateField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetIdentifier',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=160)),
                ('category', models.CharField(max_length=120)),
                ('sector', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetIdentifierSector',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=160)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetIdentifierSectorCategory',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=160)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetIdentifierVocabulary',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BudgetType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollaborationType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConditionType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(default=None, max_length=100, null=True)),
                ('organisation', models.CharField(default=None, max_length=100, null=True)),
                ('telephone', models.CharField(default=None, max_length=100, null=True)),
                ('email', models.TextField(default=None, null=True)),
                ('mailing_address', models.TextField(default=None, null=True)),
                ('website', models.CharField(default=None, max_length=255, null=True)),
                ('job_title', models.CharField(default=None, max_length=150, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CountryBudgetItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocabulary_text', models.CharField(default=None, max_length=255, null=True)),
                ('code', models.CharField(default=None, max_length=50, null=True)),
                ('percentage', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('description', models.TextField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('vocabulary', models.ForeignKey(to='iati.BudgetIdentifierVocabulary', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrsAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aid_type_flag_significance', models.IntegerField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('aid_type_flag', models.ForeignKey(to='iati.AidTypeFlag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrsAddLoanStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=None, null=True)),
                ('value_date', models.DateField(default=None, null=True)),
                ('interest_received', models.DecimalField(default=None, null=True, max_digits=15, decimal_places=2)),
                ('principal_outstanding', models.DecimalField(default=None, null=True, max_digits=15, decimal_places=2)),
                ('principal_arrears', models.DecimalField(default=None, null=True, max_digits=15, decimal_places=2)),
                ('interest_arrears', models.DecimalField(default=None, null=True, max_digits=15, decimal_places=2)),
                ('crs_add', models.ForeignKey(to='iati.CrsAdd')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrsAddLoanTerms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate_1', models.IntegerField(default=None, null=True)),
                ('rate_2', models.IntegerField(default=None, null=True)),
                ('repayment_plan_text', models.TextField(default=None, null=True)),
                ('commitment_date', models.DateField(default=None, null=True)),
                ('repayment_first_date', models.DateField(default=None, null=True)),
                ('repayment_final_date', models.DateField(default=None, null=True)),
                ('crs_add', models.ForeignKey(to='iati.CrsAdd')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=None, max_length=40000, null=True, db_index=True)),
                ('rsr_description_type_id', models.IntegerField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DescriptionType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisbursementChannel',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentCategoryCategory',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField(max_length=500)),
                ('title', models.CharField(default=None, max_length=255, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('document_category', models.ForeignKey(default=None, to='iati.DocumentCategory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ffs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extraction_date', models.DateField(default=None, null=True)),
                ('priority', models.BooleanField(default=False)),
                ('phaseout_year', models.IntegerField(max_length=4, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FfsForecast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=4, null=True)),
                ('value_date', models.DateField(default=None, null=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('currency', models.ForeignKey(to='iati.Currency')),
                ('ffs', models.ForeignKey(to='iati.Ffs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileFormat',
            fields=[
                ('code', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinanceType',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=220)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinanceTypeCategory',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlowType',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GazetteerAgency',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographicalPrecision',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographicExactness',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=None, null=True)),
                ('category', models.CharField(max_length=50)),
                ('url', models.TextField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographicLocationClass',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographicLocationReach',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographicVocabulary',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=None, null=True)),
                ('category', models.CharField(max_length=50)),
                ('url', models.TextField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanRepaymentPeriod',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanRepaymentType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.CharField(default=None, max_length=200, null=True)),
                ('name', models.TextField(default=None, max_length=1000, null=True)),
                ('type_description', models.CharField(default=None, max_length=200, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('activity_description', models.TextField(default=None, null=True)),
                ('adm_country_adm1', models.CharField(default=None, max_length=100, null=True)),
                ('adm_country_adm2', models.CharField(default=None, max_length=100, null=True)),
                ('adm_country_name', models.CharField(default=None, max_length=200, null=True)),
                ('adm_code', models.CharField(default=None, max_length=255, null=True)),
                ('adm_level', models.IntegerField(default=None, null=True)),
                ('percentage', models.DecimalField(default=None, null=True, max_digits=5, decimal_places=2)),
                ('latitude', models.CharField(default=None, max_length=70, null=True)),
                ('longitude', models.CharField(default=None, max_length=70, null=True)),
                ('gazetteer_entry', models.CharField(default=None, max_length=70, null=True)),
                ('location_id_code', models.CharField(default=None, max_length=255, null=True)),
                ('point_srs_name', models.CharField(default=None, max_length=255, null=True)),
                ('point_pos', models.CharField(default=None, max_length=255, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('adm_country_iso', models.ForeignKey(default=None, to='geodata.Country', null=True)),
                ('adm_vocabulary', models.ForeignKey(related_name=b'administrative_vocabulary   ', default=None, to='iati.GeographicVocabulary', null=True)),
                ('description_type', models.ForeignKey(default=None, to='iati.DescriptionType', null=True)),
                ('exactness', models.ForeignKey(default=None, to='iati.GeographicExactness', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationTypeCategory',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('code', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('abbreviation', models.CharField(default=None, max_length=80, null=True)),
                ('reported_by_organisation', models.CharField(default=None, max_length=100, null=True)),
                ('name', models.CharField(default=None, max_length=250, null=True)),
                ('original_ref', models.CharField(default=None, max_length=80, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganisationIdentifier',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('abbreviation', models.CharField(default=None, max_length=30, null=True)),
                ('name', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganisationRegistrationAgency',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=None, null=True)),
                ('category', models.CharField(max_length=10)),
                ('category_name', models.CharField(max_length=120)),
                ('url', models.TextField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganisationRole',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganisationType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_ref', models.CharField(default=None, max_length=100, null=True)),
                ('owner_name', models.CharField(default=None, max_length=100, null=True)),
                ('identifier', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlannedDisbursement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.CharField(default=None, max_length=100, null=True)),
                ('period_end', models.CharField(default=None, max_length=100, null=True)),
                ('value_date', models.DateField(null=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('updated', models.DateField(default=None, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('currency', models.ForeignKey(default=None, to='iati.Currency', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PolicyMarker',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PolicySignificance',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublisherType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegionVocabulary',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.CharField(default=None, max_length=200, null=True)),
                ('text', models.TextField(default=None, null=True)),
                ('current_activity', models.ForeignKey(related_name=b'current_activity', to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedActivityType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=None, max_length=255, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('aggregation_status', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(to='iati.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultIndicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=None, max_length=200, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('baseline_year', models.IntegerField(max_length=4)),
                ('baseline_value', models.CharField(max_length=100)),
                ('comment', models.TextField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultIndicatorMeasure',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultIndicatorPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.CharField(default=None, max_length=50, null=True)),
                ('period_end', models.CharField(default=None, max_length=50, null=True)),
                ('planned_disbursement_period_start', models.CharField(default=None, max_length=50, null=True)),
                ('planned_disbursement_period_end', models.CharField(default=None, max_length=50, null=True)),
                ('target', models.CharField(default=None, max_length=50, null=True)),
                ('actual', models.CharField(default=None, max_length=50, null=True)),
                ('result_indicator', models.ForeignKey(to='iati.ResultIndicator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultType',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectorCategory',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TiedStatus',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, db_index=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('language', models.ForeignKey(default=None, to='iati.Language', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=None, null=True)),
                ('provider_organisation_name', models.CharField(default=None, max_length=255, null=True)),
                ('provider_activity', models.CharField(max_length=100, null=True)),
                ('receiver_organisation_name', models.CharField(default=None, max_length=255, null=True)),
                ('transaction_date', models.DateField(default=None, null=True)),
                ('value_date', models.DateField(default=None, null=True)),
                ('value', models.DecimalField(max_digits=15, decimal_places=2)),
                ('ref', models.CharField(default=None, max_length=255, null=True)),
                ('activity', models.ForeignKey(to='iati.Activity')),
                ('aid_type', models.ForeignKey(default=None, to='iati.AidType', null=True)),
                ('currency', models.ForeignKey(default=None, to='iati.Currency', null=True)),
                ('description_type', models.ForeignKey(default=None, to='iati.DescriptionType', null=True)),
                ('disbursement_channel', models.ForeignKey(default=None, to='iati.DisbursementChannel', null=True)),
                ('finance_type', models.ForeignKey(default=None, to='iati.FinanceType', null=True)),
                ('flow_type', models.ForeignKey(default=None, to='iati.FlowType', null=True)),
                ('provider_organisation', models.ForeignKey(related_name=b'transaction_providing_organisation', default=None, to='iati.Organisation', null=True)),
                ('receiver_organisation', models.ForeignKey(related_name=b'transaction_receiving_organisation', default=None, to='iati.Organisation', null=True)),
                ('tied_status', models.ForeignKey(default=None, to='iati.TiedStatus', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValueType',
            fields=[
                ('code', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VerificationStatus',
            fields=[
                ('code', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.ForeignKey(default=None, to='iati.TransactionType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sector',
            name='category',
            field=models.ForeignKey(default=None, to='iati.SectorCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultindicator',
            name='measure',
            field=models.ForeignKey(default=None, to='iati.ResultIndicatorMeasure', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultindicator',
            name='result',
            field=models.ForeignKey(to='iati.Result'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='result_type',
            field=models.ForeignKey(default=None, to='iati.ResultType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedactivity',
            name='type',
            field=models.ForeignKey(default=None, to='iati.RelatedActivityType', max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organisation',
            name='type',
            field=models.ForeignKey(default=None, to='iati.OrganisationType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationtype',
            name='category',
            field=models.ForeignKey(to='iati.LocationTypeCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='feature_designation',
            field=models.ForeignKey(related_name=b'feature_designation', default=None, to='iati.LocationType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='gazetteer_ref',
            field=models.ForeignKey(default=None, to='iati.GazetteerAgency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='location_class',
            field=models.ForeignKey(default=None, to='iati.GeographicLocationClass', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='location_id_vocabulary',
            field=models.ForeignKey(related_name=b'location_id_vocabulary', default=None, to='iati.GeographicVocabulary', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='location_reach',
            field=models.ForeignKey(default=None, to='iati.GeographicLocationReach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='precision',
            field=models.ForeignKey(default=None, to='iati.GeographicalPrecision', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.ForeignKey(related_name=b'deprecated_location_type', default=None, to='iati.LocationType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='financetype',
            name='category',
            field=models.ForeignKey(to='iati.FinanceTypeCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentlink',
            name='file_format',
            field=models.ForeignKey(default=None, to='iati.FileFormat', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='category',
            field=models.ForeignKey(to='iati.DocumentCategoryCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='language',
            field=models.ForeignKey(default=None, to='iati.Language', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='type',
            field=models.ForeignKey(related_name=b'description_type', default=None, to='iati.DescriptionType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crsaddloanterms',
            name='repayment_plan',
            field=models.ForeignKey(default=None, to='iati.LoanRepaymentPeriod', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crsaddloanterms',
            name='repayment_type',
            field=models.ForeignKey(default=None, to='iati.LoanRepaymentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crsaddloanstatus',
            name='currency',
            field=models.ForeignKey(default=None, to='iati.Currency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='contact_type',
            field=models.ForeignKey(default=None, to='iati.ContactType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='condition',
            name='type',
            field=models.ForeignKey(default=None, to='iati.ConditionType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budgetidentifiersector',
            name='category',
            field=models.ForeignKey(to='iati.BudgetIdentifierSectorCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budget',
            name='currency',
            field=models.ForeignKey(default=None, to='iati.Currency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budget',
            name='type',
            field=models.ForeignKey(default=None, to='iati.BudgetType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aidtype',
            name='category',
            field=models.ForeignKey(to='iati.AidTypeCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitysector',
            name='sector',
            field=models.ForeignKey(default=None, to='iati.Sector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitysector',
            name='vocabulary',
            field=models.ForeignKey(default=None, to='iati.Vocabulary', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityrecipientregion',
            name='region_vocabulary',
            field=models.ForeignKey(default=1, to='iati.RegionVocabulary'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitypolicymarker',
            name='policy_marker',
            field=models.ForeignKey(default=None, to='iati.PolicyMarker', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitypolicymarker',
            name='policy_significance',
            field=models.ForeignKey(default=None, to='iati.PolicySignificance', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitypolicymarker',
            name='vocabulary',
            field=models.ForeignKey(default=None, to='iati.Vocabulary', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityparticipatingorganisation',
            name='organisation',
            field=models.ForeignKey(default=None, to='iati.Organisation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityparticipatingorganisation',
            name='role',
            field=models.ForeignKey(default=None, to='iati.OrganisationRole', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_status',
            field=models.ForeignKey(default=None, to='iati.ActivityStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='collaboration_type',
            field=models.ForeignKey(default=None, to='iati.CollaborationType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='default_aid_type',
            field=models.ForeignKey(default=None, to='iati.AidType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='default_currency',
            field=models.ForeignKey(related_name=b'default_currency', default=None, to='iati.Currency', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='default_finance_type',
            field=models.ForeignKey(default=None, to='iati.FinanceType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='default_flow_type',
            field=models.ForeignKey(default=None, to='iati.FlowType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='default_tied_status',
            field=models.ForeignKey(default=None, to='iati.TiedStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='participating_organisation',
            field=models.ManyToManyField(to='iati.Organisation', through='iati.ActivityParticipatingOrganisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='policy_marker',
            field=models.ManyToManyField(to='iati.PolicyMarker', through='iati.ActivityPolicyMarker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='recipient_country',
            field=models.ManyToManyField(to='geodata.Country', through='iati.ActivityRecipientCountry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='recipient_region',
            field=models.ManyToManyField(to='geodata.Region', through='iati.ActivityRecipientRegion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='reporting_organisation',
            field=models.ForeignKey(related_name=b'activity_reporting_organisation', default=None, to='iati.Organisation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='scope',
            field=models.ForeignKey(default=None, to='iati.ActivityScope', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='sector',
            field=models.ManyToManyField(to='iati.Sector', through='iati.ActivitySector'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='total_budget_currency',
            field=models.ForeignKey(related_name=b'total_budget_currency', default=None, to='iati.Currency', null=True),
            preserve_default=True,
        ),
    ]
