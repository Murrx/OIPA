from parseit import parser
from lxml import etree


def test_parse_description():
    description_elem = etree.fromstring(
        '<description type="3">Statement of groups targeted to benefit from the activity.</description>'
    )
    description = parser.parse_description(description_elem)
    assert description.description == 'Statement of groups targeted to benefit from the activity.'
    assert description.type_id == 3
