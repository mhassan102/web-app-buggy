from flask import request


def calc():
    expr = request.args.get("expr", "")
    try:
        return str(eval(expr))  # BUG: eval — expr from the query string is evaluated as Python
    except Exception:
        return ""
