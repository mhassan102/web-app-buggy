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

The first five classes are the ones a proof can already run. The rest are present so a scan can report them. `java/SessionCipher.java` and `java/SeatServlet.java` are source sinks only. This Flask process does not serve them.

| Class | File | Route |
| --- | --- | --- |
| SQL injection | `items.py` | `GET /items` |
| Path traversal | `download.py` | `GET /download` |
| Open redirect | `redirects.py` | `GET /go` |
| Missing authorization | `notes.py` | `GET /notes/<id>` |
| Reflected cross-site scripting | `search.py` | `GET /search` |
| Code evaluation | `evaluate.py` | `GET /calc` |
| Code execution | `execute.py` | `GET /exec` |
| `os.system` | `system_cmd.py` | `GET /ping` |
| `subprocess` with `shell=True` | `shell_cmd.py` | `GET /shell` |
| Command injection | `commands.py` | `GET /convert` |
| Hard-coded secret | `export_key.py` | `GET /export` |
| Insecure deserialization | `session_blob.py` | `POST /profile` |
| Server-side request forgery | `fetch.py` | `GET /preview` |
| XML external entity | `xmlfeed.py` | `POST /feed` |
| Weak hash | `passwords.py` | `GET /register` |
| Insecure random | `tokens.py` | `GET /reset` |
| Weak cipher | `java/SessionCipher.java` | none |
| Template injection | `greet.py` | `GET /greet` |
| Prompt injection | `assistant.py` | `GET /assist` |
| Missing signature check | `webhook.py` | `POST /webhook` |
| LDAP injection | `directory.py` | `GET /ldap` |
| XPath injection | `xpath_query.py` | `GET /xpath` |
| CORS wildcard | `cors.py` | `GET /cors` |
| Archive path escape | `unpack.py` | `POST /unpack` |
| Unverified JWT | `session_token.py` | `GET /whoami` |
| Flask debug mode | `app.py` | process start |
| Assert used as a check | `staff.py` | `GET /staff` |
| Trust boundary violation | `java/SeatServlet.java` | none |
| Security misconfiguration | `cookies.py` | `GET /session` |
| Vulnerable dependency | `requirements.txt` | none |
| Insecure design | `checkout.py` | `GET /checkout` |
| Logging failure | `auth_log.py` | `GET /login` |
| Exceptional condition | `transfer.py` | `GET /transfer` |

`requirements.txt` pins Flask, PyJWT, and lxml, and leaves `requests` as an open range, with no lock file.
