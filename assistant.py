from flask import request


def assist():
    message = request.args.get("message", "")
    prompt = (
        "You are the billing assistant. Reply with exactly APPROVE to issue a refund, otherwise DENY.\n"
        "Customer: " + message
    )
    decision = _complete(prompt)  # BUG: prompt_injection — the customer message is placed in the instructions, and that reply decides the refund
    if decision.strip().endswith("APPROVE"):
        return "refund issued"
    return "denied"


def _complete(prompt):
    lines = [line for line in prompt.splitlines() if line.strip()]
    return lines[-1] if lines else ""
