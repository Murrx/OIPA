from django.http import HttpResponse
from iati_synchroniser import models
import json


def request_parse_url_view(request):
    publisher_ref = request.GET.get('publisher_ref')
    publisher_name = request.GET.get('publisher_name')
    xml_source_url = request.GET.get('xml_source_url')
    xml_ref = request.GET.get('xml_ref')

    result = {'parsed': False}

    try:
        publisher = models.Publisher.objects.get(org_id=publisher_ref)
        result['publisher'] = 'exists'
    except models.Publisher.DoesNotExist:
        publisher = models.Publisher.objects.create(org_id=publisher_ref, org_name=publisher_name)
        result['publisher'] = 'does_not_exist'

    try:
        xml_source = models.IatiXmlSource.objects.get(ref=xml_ref, source_url=xml_source_url)
        result['iati_xml_source'] = 'exists'

    except models.IatiXmlSource.DoesNotExist:
        xml_source = models.IatiXmlSource.objects.create(ref=xml_ref, source_url=xml_source_url, publisher=publisher)
        result['iati_xml_source'] = 'does_not_exist'

    xml_source.save()

    result['parsed'] = True

    return HttpResponse(json.dumps(result), content_type="application/json")
