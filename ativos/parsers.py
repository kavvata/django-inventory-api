import decimal
from datetime import datetime
from xml.etree.ElementTree import Element

from defusedxml import ElementTree
from django.conf import settings
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser


class XMLParser(BaseParser):
    media_type = "application/xml"

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)
        parser = ElementTree.DefusedXMLParser(encoding=encoding)
        try:
            tree = ElementTree.parse(stream, parser=parser, forbid_dtd=True)
        except (ElementTree.ParseError, ValueError) as exc:
            raise ParseError("XML parse error - %s" % str(exc))
        data = self._xml_convert(tree.getroot())
        return data

    def _xml_convert(self, element: Element):
        """
        convert the xml `element` into the corresponding python object
        """

        children = list(element)
        if len(children) == 0:
            return element.text

        sub_tags = []

        for child in children:
            if child.tag not in sub_tags:
                sub_tags.append(child.tag)

        final_data = {}

        for tag in sub_tags:
            elements_with_same_tag = element.findall(tag)

            if len(elements_with_same_tag) > 1:
                data = []
                for child in elements_with_same_tag:
                    data.append(self._xml_convert(child))

            else:
                data = self._xml_convert(elements_with_same_tag[0])

            final_data[tag] = data

        return final_data

    def _type_convert(self, value):
        """
        Converts the value returned by the XMl parse into the equivalent
        Python type
        """
        if value is None:
            return value

        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return decimal.Decimal(value)
        except decimal.InvalidOperation:
            pass

        return value
