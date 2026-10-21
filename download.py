import os

from flask import abort, request

FILES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


def download():
    name = request.args.get("file", "")
    try:
        with open(os.path.join(FILES, name), encoding="utf-8", errors="replace") as handle:  # BUG: path_traversal — file is joined onto the downloads directory and opened
            body = handle.read()
    except OSError:
        abort(404)
    return body
