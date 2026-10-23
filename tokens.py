import random

from flask import request


def reset_token():
    user = request.args.get("user", "")
    token = "%s-%s" % (user, random.randint(0, 999999))  # BUG: insecure_random — the reset token comes from the random module
    return token
