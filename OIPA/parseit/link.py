import os
import sys
# Ugliest code ever to get OIPA's root directory
OIPA_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(OIPA_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'OIPA.settings'
# import django
# django.setup()

from lxml import etree
from iati import models


class Mapper:
    pass


class ElementMapper(Mapper):
    def __init__(self, xml_name, parser):
        self._xml_name = xml_name
        self._parser = parser


class AttributeMapper(Mapper):
    def __init__(self, xml_name):
        self._xml_name = xml_name


class GenericParser:
    def register_mappers(self):
        attributes = [a for a in dir(self) if not callable(a)]
        for attr_str in attributes:
            attr = getattr(self, attr_str)
            if isinstance(attr, Mapper):
                attr._fieldname = attr_str
                if isinstance(attr, ElementMapper):
                    self._elements[attr._xml_name] = attr
                if isinstance(attr, AttributeMapper):
                    self._attributes[attr._xml_name] = attr

    def __init__(self, element):
        self._xml_element = element
        self._object_instance = None
        self._exception_log = 'Need to create a log class'
        self._attributes = dict()
        self._elements = dict()
        self.register_mappers()

    def parse(self):
        # self._instance = self.Meta.model()
        print 'PARSING: {0}'.format(self.Meta.model)

        # Parse attributes
        for name, value in self._xml_element.items():
            if name in self._attributes:
                mapper = self._attributes.get(name)
                print 'mapping found for attribute: {0} = {1}'.format(
                    name, value)

        # Parse freetext
        if hasattr(self.Meta, 'freetext'):
            print 'mapping found for freetext: {0}'.format(
                self._xml_element.text)
        print ''

        # Parse elements
        for element in self._xml_element.iterchildren():
            if element.tag in self._elements:
                mapper = self._elements.get(element.tag)
                print 'mapping found for element: {0}'.format(element)
                parser = mapper._parser(element)
                parser.parse()


class DescriptionParser(GenericParser):
    type = AttributeMapper('type')

    class Meta:
        tag = 'description'
        model = models.Description
        freetext = 'description'


class ActivityParser(GenericParser):
    default_currency = AttributeMapper('default-currency')
    iati_standard_version = AttributeMapper('version')
    description = ElementMapper('description', DescriptionParser)

    class Meta:
        tag = 'iati-activity'
        model = models.Activity


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
