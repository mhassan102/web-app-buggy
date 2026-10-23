from flask import request


def run_code():
    code = request.args.get("code", "")
    namespace = {}
    try:
        exec(code, namespace)  # BUG: exec — code from the query string is executed
    except Exception:
        return ""
    return str(namespace.get("result", ""))
