import traceback

from flask import request


def transfer():
    amount = request.args.get("amount", "0")
    try:
        _require_admin()
        cents = int(amount)
    except Exception:
        return "transferred\n" + traceback.format_exc()  # BUG: exceptional_condition — a failed authorization check still transfers, and the traceback is returned to the caller
    return "transferred %s" % cents


def _require_admin():
    header = request.headers.get("Authorization", "")
    if header != "Bearer admin":
        raise PermissionError("denied")
