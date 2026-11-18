import os
from flask import Flask

from cart_update import bp as cart_update_bp
from collect_policy import bp as collect_policy_bp
from format_manifest import bp as format_manifest_bp
from archive_manifest import bp as archive_manifest_bp
from publish_schedule import bp as publish_schedule_bp
from compact_cart import bp as compact_cart_bp
from compact_manifest import bp as compact_manifest_bp
from validate_order import bp as validate_order_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(cart_update_bp)
app.register_blueprint(collect_policy_bp)
app.register_blueprint(format_manifest_bp)
app.register_blueprint(archive_manifest_bp)
app.register_blueprint(publish_schedule_bp)
app.register_blueprint(compact_cart_bp)
app.register_blueprint(compact_manifest_bp)
app.register_blueprint(validate_order_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
