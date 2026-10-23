from flask import make_response


def cors():
    response = make_response("ok")
    response.headers["Access-Control-Allow-Origin"] = "*"  # BUG: cors_wildcard — every origin is allowed
    return response
