from flask import redirect, request


def go():
    target = request.args.get("next", "/")
    return redirect(target)  # BUG: open_redirect — next is used as the redirect location
