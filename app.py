import argparse

from flask import Flask

from download import download
from items import items
from notes import get_note, list_notes
from redirects import go
from search import bp as search_bp

app = Flask(__name__)
app.register_blueprint(search_bp)
app.add_url_rule("/health", "health", lambda: "ok")
app.add_url_rule("/items", "items", items)
app.add_url_rule("/download", "download", download)
app.add_url_rule("/go", "go", go)
app.add_url_rule("/notes", "list_notes", list_notes)
app.add_url_rule("/notes/<int:note_id>", "get_note", get_note)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)
