import urllib.request

from flask import request


def preview():
    target = request.args.get("url", "")
    try:
        with urllib.request.urlopen(target, timeout=3) as resp:  # BUG: ssrf — url is fetched by the server
            body = resp.read(512)
    except (OSError, ValueError):
        return "fetch failed"
    return body
