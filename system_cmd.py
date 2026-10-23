import os

from flask import request


def ping():
    host = request.args.get("host", "")
    status = os.system("ping -c 1 " + host)  # BUG: os_system — host is concatenated into a shell command
    return str(status)
