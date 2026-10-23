from flask import request


def payment_webhook():
    event = request.get_json(force=True, silent=True) or {}
    request.headers.get("X-Signature", "")
    if event.get("type") == "payment.succeeded":
        return "order %s marked paid" % event.get("order_id", "")  # BUG: signature_unverified — the payment event is applied and the signature header is never checked
    return "ignored"
