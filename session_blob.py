import pickle

from flask import request


def load_profile():
    raw = request.get_data()
    try:
        return str(pickle.loads(raw))  # BUG: insecure_deserialization — request bytes are unpickled
    except Exception:
        return ""
