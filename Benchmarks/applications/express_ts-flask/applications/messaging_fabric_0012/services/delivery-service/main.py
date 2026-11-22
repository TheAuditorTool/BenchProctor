import os
from flask import Flask

from delivery_dispatch import bp as delivery_dispatch_bp
from load_subscription import bp as load_subscription_bp
from publish_roster import bp as publish_roster_bp
from archive_receipt import bp as archive_receipt_bp
from enrich_delivery import bp as enrich_delivery_bp
from resolve_window import bp as resolve_window_bp
from compact_profile import bp as compact_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(delivery_dispatch_bp)
app.register_blueprint(load_subscription_bp)
app.register_blueprint(publish_roster_bp)
app.register_blueprint(archive_receipt_bp)
app.register_blueprint(enrich_delivery_bp)
app.register_blueprint(resolve_window_bp)
app.register_blueprint(compact_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
