from flask import request


def whoami():
    header = request.headers.get("Authorization", "")
    token = header.removeprefix("Bearer ").strip()
    if not token:
        return ""
    import jwt
    try:
        claims = jwt.decode(token, options={"verify_signature": False})  # BUG: jwt_unverified — the signature is not checked and sub is trusted
    except Exception:
        return ""
    return str(claims.get("sub", ""))
