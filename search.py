from flask import Blueprint, request

bp = Blueprint("search", __name__)


@bp.get("/search")
def search():
    q = request.args.get("q", "")
    return "<h1>Results</h1><p>" + q + "</p>"  # BUG: xss (reflected) — q is placed in the HTML response without escaping
