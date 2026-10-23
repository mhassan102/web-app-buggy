from flask import render_template_string, request


def greet():
    name = request.args.get("name", "")
    return render_template_string(name)  # BUG: template_injection — name is compiled as a template
