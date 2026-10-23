import logging

from flask import request

log = logging.getLogger("buggy.auth")


def login():
    username = request.args.get("user", "")
    password = request.args.get("password", "")
    log.info("login user=%s password=%s", username, password)  # BUG: logging_failure — the password is written to the log, and a denied login is not recorded
    if not password:
        return "denied"
    return "ok"
