from lxml import etree
from iati import models
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def retrieve_attribute(element, attribute):
    print "none"


def retrieve_element_value(element, name):
    retrieved_element = element.find(name)
    if retrieved_element is None:
        logger.info("retrieve_element_value: %s is null" % (name))
    else:
        logger.debug("retrieve_element_value: %s (%s) is %s" % (
            name, retrieved_element.tag, retrieved_element.text))
        return retrieved_element.text


def parse_reporting_org(element):
    ref = element.get("ref", default=None)
    type = element.get("type", default=None)
    organisation_name = element.text

    logger.debug("parse_reporting_org: %s, %s, %s" % (
        ref, type, organisation_name,))
    # Do stuff with model
    # Return model


def parse_iati_identifier(element):
    iati_identifier = element.text
    logger.debug("parse_iati_identifier: %s" % (iati_identifier))


def parse_other_identifier(element):
    owner_name = element.get("owner-name", default=None)
    owner_ref = element.get("owner-ref", default=None)
    other_identifier = element.text

    logger.debug("parse_other_identifier: %s, %s, %s" % (
        owner_name, owner_ref, other_identifier))


def parse_title(element):
    title = element.text

    logger.debug("parse_title: %s" % (title))


def parse_description(element):
    mapping_dict = {
        'type': {'function': (lambda value: int(value)), 'field': 'type_id'}
    }
    object_dict = {}

    for name, value in element.items():
        dict_row = mapping_dict[name]
        object_dict[dict_row['field']] = dict_row['function'](value)
    object_dict['description'] = element.text

    return models.Description(**object_dict)


def parse_activity_status(element):
    activity_status = element.get("code", default=None)

    logger.debug("parse_activity_status: %s" % (activity_status))


def parse_activity_date(element):
    iso_date = element.get("iso-date", default=None)
    activity_date_type = element.get("type", default=None)

    logger.debug("parse_activity_date: %s (%s)" % (
        iso_date, activity_date_type))


def parse_contact_info(element):

    def parse_type(element):
        print "type"

    def parse_organisation(element):
        print "org"

    def parse_job_title(element):
        print "title"

    def parse_telephone(element):
        print 'tel'

    def parse_email(element):
        print "email"

    def parse_mailing_address(element):
        print "mailing-address"

    def parse_website(element):
        print "website"

    contact_info_parsers = {
        'type': parse_type,
        'organisation': parse_organisation,
        'job-title': parse_job_title,
        'telephone': parse_telephone,
        'email': parse_email,
        'mailing-address': parse_mailing_address,
        'website': parse_website
    }
    contact_type = element.get("type", default=None)

    # TODO: None.text is not allowed checks!
    organisation = element.find("organisation").text
    job_title = element.find("job-title").text
    telephone = element.find("telephone").text
    email = element.find("email").text
    mailing_address = element.find("mailing-address").text
    website = retrieve_element_value(element, "website")

    logger.debug("parse_contact_info: %s (%s)" % (organisation, contact_type))
    logger.debug("parse_contact_info: %s - %s - %s" % (
        job_title, telephone, email))
    logger.debug("parse_contact_info: %s" % (mailing_address))
    logger.debug("parse_contact_info: %s" % (website))


def parse_undefined_element(element):
    logger.warn("parse_undefined_element: %s" % (element.tag))


parser_105_dictionary = {
    'reporting-org': parse_reporting_org,
    'iati-identifier': parse_iati_identifier,
    'other-identifier': parse_other_identifier,
    'title': parse_title,
    'description': parse_description,
    'activity-status': parse_activity_status,
    'activity-date': parse_activity_date,
    'contact-info': parse_contact_info
}


def parse_file(url):
    # root = etree.parse(url)
    parse_xml(url)


def parse_xml(xml_file):
    for _, element in etree.iterparse(
            xml_file, tag="iati-activity", remove_comments=True):
        print "Iati activity"
        parse_activity(element)


def parse_activity(activity_element):
    xml_lang = activity_element.get("lang", default=None)  # TODO: not working
    version = activity_element.get("version", default=None)
    generated_datetime = activity_element.get(
        "generated-datetime", default=None)
    default_currency = activity_element.get(
        "default-currency", default=None)
    hierarchy = activity_element.get("hierarchy", default=None)
    linked_data_uri = activity_element.get("linked-data-uri", default=None)

    logger.debug("parse_activity: attribute xml:lang: %s" % (xml_lang))
    logger.debug("parse_activity: attribute version: %s" % (version))
    logger.debug("parse_activity: attribute generated-datetime: %s" % (
        generated_datetime))
    logger.debug("parse_activity: attribute default-currency: %s" % (
        default_currency))
    logger.debug("parse_activity: attribute hierarchy: %s" % (hierarchy))
    logger.debug("parse_activity: attribute linked-data-uri: %s" % (
        linked_data_uri))

    for element in activity_element:
        result = parser_105_dictionary.get(
            element.tag, parse_undefined_element)(element)


if __name__ == "__main__":
    parse_file("activity-standard-example-annotated.xml")
