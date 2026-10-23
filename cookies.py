from flask import make_response


def session_cookie():
    response = make_response("signed-in")
    response.set_cookie(  # BUG: security_misconfiguration — the session cookie is sent with Secure and HttpOnly off and no SameSite
        "session",
        "admin-session",
        secure=False,
        httponly=False,
        samesite=None,
    )
    return response
