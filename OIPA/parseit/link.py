import os
import sys
# Ugliest code ever to get OIPA's root directory
OIPA_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(OIPA_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'OIPA.settings'

from lxml import etree
from iati import models


class ElementMapper:
    def __init__(self, xml_name, parser):
        self._xml_name = xml_name
        self._parser = parser


class AttributeMapper:
    def __init__(self, xml_name):
        self._xml_name = xml_name


class GenericParser:
    def __init__(self, element):
        self._xml_element = element
        self._object_instance = self.Meta.model
        self._exception_log = 'Need to create a log class'

    def parse(self):
        print 'PARSING: {0}'.format(self._object_instance)

        # Parse attributes
        for name, value in self._xml_element.items():
            print '{0}: {1}'.format(name, value)

        # Parse freetext
        if hasattr(self.Meta, 'freetext'):
            print self._xml_element.text
        print ''

        # Parse elements
        for element in self._xml_element.iterchildren():
            try:
                if element.tag in self.Meta.elements:
                    mapper = getattr(self, 'description')
                    parser = mapper._parser(element)
                    parser.parse()
            except AttributeError as e:
                print e


class DescriptionParser(GenericParser):
    type = AttributeMapper('type')

    class Meta:
        tag = 'description'
        model = models.Description
        attributes = ('type',)
        freetext = 'description'


class ActivityParser(GenericParser):
    default_currency = AttributeMapper('default-currency')
    iati_standard_version = AttributeMapper('version')
    description = ElementMapper('description', DescriptionParser)

    class Meta:
        tag = 'iati-activity'
        model = models.Activity
        attributes = ('default_currency', 'version',)
        elements = ('description',)


def parse_xml(xml_file):
    for _, element in etree.iterparse(
        xml_file,
        tag='iati-activity',
        remove_comments=True
    ):
        parser = ActivityParser(element)
        parser.parse()


if __name__ == "__main__":
    parse_xml("activity-standard-example-annotated.xml")
