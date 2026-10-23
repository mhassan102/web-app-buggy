from flask import request
from lxml import etree


def feed():
    body = request.get_data()
    parser = etree.XMLParser(resolve_entities=True)
    try:
        root = etree.fromstring(body, parser)  # BUG: xxe — the request body is parsed with external entities resolved
    except etree.XMLSyntaxError:
        return ""
    return etree.tostring(root, encoding="unicode")
