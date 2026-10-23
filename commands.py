import os

from flask import request


def convert():
    path = request.args.get("path", "")
    pipe = os.popen("ls " + path)  # BUG: command_injection — path is concatenated into a shell command
    try:
        return pipe.read()
    finally:
        pipe.close()
