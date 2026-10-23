import hashlib

from flask import request


def register():
    password = request.args.get("password", "")
    return hashlib.md5(password.encode()).hexdigest()  # BUG: weak_hash — the password is hashed with MD5
