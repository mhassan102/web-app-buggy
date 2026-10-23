from flask import request


class Catalog:
    def xpath(self, query):
        return query


catalog = Catalog()


def find_user():
    name = request.args.get("name", "")
    return catalog.xpath("//user[name='" + name + "']")  # BUG: xpath_injection — name is concatenated into the XPath query
