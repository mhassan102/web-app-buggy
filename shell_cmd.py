import subprocess

from flask import request


def shell():
    name = request.args.get("name", "")
    completed = subprocess.run(f"echo {name}", shell=True, capture_output=True, text=True)  # BUG: subprocess_shell — name is interpolated into a shell command
    return completed.stdout
