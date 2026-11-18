import os
from flask import Flask

from order_lookup import bp as order_lookup_bp
from normalize_fulfillment import bp as normalize_fulfillment_bp
from fetch_roster import bp as fetch_roster_bp
from annotate_schedule import bp as annotate_schedule_bp
from resolve_roster import bp as resolve_roster_bp
from compact_roster import bp as compact_roster_bp
from compact_cart import bp as compact_cart_bp
from prune_receipt import bp as prune_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(order_lookup_bp)
app.register_blueprint(normalize_fulfillment_bp)
app.register_blueprint(fetch_roster_bp)
app.register_blueprint(annotate_schedule_bp)
app.register_blueprint(resolve_roster_bp)
app.register_blueprint(compact_roster_bp)
app.register_blueprint(compact_cart_bp)
app.register_blueprint(prune_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
