from flask import abort, request

api_key = "sk-buggy-7f3c91d2e88a0c4"  # BUG: hardcoded_secret — the export key is a literal in source


def export_users():
    supplied = request.headers.get("X-Api-Key", "")
    if supplied != api_key:
        abort(401)
    return "alice,bob"
