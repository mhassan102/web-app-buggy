from flask import request


def staff():
    role = request.args.get("role", "")
    assert role == "admin"  # BUG: assert_used — the admin check is an assert, which Python removes under -O
    return "staff directory"
