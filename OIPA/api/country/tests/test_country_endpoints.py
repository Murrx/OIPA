from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCountryEndpoints(TestCase):

    def test_countries_endpoint(self):
        url = reverse('countries:country-list')

        msg = 'countries endpoint should be localed at {0}'
        expect_url = '/api/countries/'
        assert url == expect_url, msg.format(expect_url)

    def test_country_detail_endpoint(self):
        url = reverse('countries:country-detail', args={'id'})

        msg = 'country detail endpoint should be localed at {0}'
        expect_url = '/api/countries/id/'
        assert url == expect_url, msg.format(expect_url)

    def test_country_activities_endpoint(self):
        url = reverse('countries:country-activities', args={'id'})

        msg = 'country detail endpoint should be localed at {0}'
        expect_url = '/api/countries/id/activities/'
        assert url == expect_url, msg.format(expect_url)

    def test_country_indicators_endpoint(self):
        url = reverse('countries:country-indicators', args={'id'})

        msg = 'country detail endpoint should be localed at {0}'
        expect_url = '/api/countries/id/indicators/'
        assert url == expect_url, msg.format(expect_url)

    def test_country_cities_endpoint(self):
        url = reverse('countries:country-cities', args={'id'})

        msg = 'country detail endpoint should be localed at {0}'
        expect_url = '/api/countries/id/cities/'
        assert url == expect_url, msg.format(expect_url)
