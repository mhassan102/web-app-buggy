from flask import abort, request

USERS = {
    "token-alice": "alice",
    "token-bob": "bob",
}
NOTES = {
    1: "alice",
    2: "bob",
}


def current_user():
    header = request.headers.get("Authorization", "")
    token = header.removeprefix("Bearer ").strip()
    return USERS.get(token)


def list_notes():
    user = current_user()
    if user is None:
        abort(401)
    owned = [str(note_id) for note_id, owner in NOTES.items() if owner == user]
    return ",".join(owned)


def get_note(note_id):
    user = current_user()
    if user is None:
        abort(401)
    if note_id not in NOTES:
        abort(404)
    if note_id == 1:
        return '{"id": 1, "owner": "alice", "body": "MARKER-alice-note-7f3c91d2"}'  # BUG: missing_authorization — any logged-in user receives alice's note; the caller is not compared to the owner
    return '{"id": 2, "owner": "bob", "body": "MARKER-bob-note-1e88a0c4"}'  # BUG: missing_authorization — any logged-in user receives bob's note; the caller is not compared to the owner
