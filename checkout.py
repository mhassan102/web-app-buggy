from flask import request


def checkout():
    price = request.args.get("price", "0")
    quantity = request.args.get("quantity", "1")
    return "charged %s x %s" % (price, quantity)  # BUG: insecure_design — the client sets the price and the quantity, and the server never checks either
