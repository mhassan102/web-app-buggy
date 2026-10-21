# Buggy Python web app

A small Flask application with intentional security bugs. It exists so a vulnerability scanner can be pointed at this repository and checked against known weaknesses.

Do not run this app on a server. Do not expose it to a network, a shared host, or the public internet. The bugs are real, and this tree is not safe to deploy.

## Run locally

```bash
pip install -r requirements.txt
python app.py --port 8080
```

A readiness check is `GET /health`.

## Marked bugs

Each weakness is commented on the line where it lives. Search the source for `BUG:`.

| Class | File |
| --- | --- |
| SQL injection | `items.py` |
| Path traversal | `download.py` |
| Open redirect | `redirects.py` |
| Missing authorization | `notes.py` |
| Reflected cross-site scripting | `search.py` |
