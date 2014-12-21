from lxml import etree


class GenericParser:
    _object_instance = None
    _xml_element = None
    _exception_log = None

    def __init__(self, element):
        self._xml_element = element
        self._object_instance = self.Meta.model
        self._exception_log = 'Need to create a log class'

    def parse(self):
        print 'PARSING: {0}'.format(self._object_instance)
        for name, value in self._xml_element.items():
            print '{0}: {1}'.format(name, value)
        if self.freetext:
            print self._xml_element.text
        print ''

        if len(self._xml_element):  # check if the element has children
            print 'PARSING CHILDREN:'
        for element in self._xml_element.iterchildren():
            if element.tag in self.elements:
                child_parser_class = self.elements[element.tag]['parser']
                child_parser = child_parser_class(element)
                child_parser.parse()


class DescriptionParser(GenericParser):
    class Meta:
        tag = 'description'
        model = 'iati.models.Descripion'

    items = {'type': 'type_id', }
    elements = None
    freetext = True


class ActivityParser(GenericParser):
    class Meta:
        tag = 'iati-activity'
        model = 'iati.models.Activity'

    items = {
        'deafult-currency': 'default_currency',
        'version': 'iati_standard_version',
    }
    elements = {
        'description': {
            'parser': DescriptionParser,
            'relation': 'description_set'},
    }
    freetext = None


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
