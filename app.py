import argparse

from flask import Flask

from assistant import assist
from auth_log import login
from checkout import checkout
from commands import convert
from cookies import session_cookie
from cors import cors
from directory import ldap_lookup
from download import download
from evaluate import calc
from execute import run_code
from export_key import export_users
from fetch import preview
from greet import greet
from items import items
from notes import get_note, list_notes
from passwords import register
from redirects import go
from search import bp as search_bp
from session_blob import load_profile
from session_token import whoami
from shell_cmd import shell
from staff import staff
from system_cmd import ping
from tokens import reset_token
from transfer import transfer
from unpack import unpack
from webhook import payment_webhook
from xmlfeed import feed
from xpath_query import find_user

app = Flask(__name__)
app.register_blueprint(search_bp)
app.add_url_rule("/health", "health", lambda: "ok")
app.add_url_rule("/items", "items", items)
app.add_url_rule("/download", "download", download)
app.add_url_rule("/go", "go", go)
app.add_url_rule("/notes", "list_notes", list_notes)
app.add_url_rule("/notes/<int:note_id>", "get_note", get_note)
app.add_url_rule("/calc", "calc", calc)
app.add_url_rule("/exec", "run_code", run_code)
app.add_url_rule("/ping", "ping", ping)
app.add_url_rule("/shell", "shell", shell)
app.add_url_rule("/convert", "convert", convert)
app.add_url_rule("/export", "export_users", export_users)
app.add_url_rule("/profile", "load_profile", load_profile, methods=["POST"])
app.add_url_rule("/preview", "preview", preview)
app.add_url_rule("/feed", "feed", feed, methods=["POST"])
app.add_url_rule("/register", "register", register)
app.add_url_rule("/reset", "reset_token", reset_token)
app.add_url_rule("/greet", "greet", greet)
app.add_url_rule("/assist", "assist", assist)
app.add_url_rule("/webhook", "payment_webhook", payment_webhook, methods=["POST"])
app.add_url_rule("/ldap", "ldap_lookup", ldap_lookup)
app.add_url_rule("/xpath", "find_user", find_user)
app.add_url_rule("/cors", "cors", cors)
app.add_url_rule("/unpack", "unpack", unpack, methods=["POST"])
app.add_url_rule("/whoami", "whoami", whoami)
app.add_url_rule("/staff", "staff", staff)
app.add_url_rule("/session", "session_cookie", session_cookie)
app.add_url_rule("/checkout", "checkout", checkout)
app.add_url_rule("/login", "login", login)
app.add_url_rule("/transfer", "transfer", transfer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port, debug=True)  # BUG: flask_debug — the debugger is switched on
