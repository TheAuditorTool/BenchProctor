import os
from flask import Flask

from tracking_poll import bp as tracking_poll_bp
from validate_profile import bp as validate_profile_bp
from prune_label import bp as prune_label_bp
from enrich_header import bp as enrich_header_bp
from compact_shipment import bp as compact_shipment_bp
from enrich_summary import bp as enrich_summary_bp
from reconcile_config import bp as reconcile_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(tracking_poll_bp)
app.register_blueprint(validate_profile_bp)
app.register_blueprint(prune_label_bp)
app.register_blueprint(enrich_header_bp)
app.register_blueprint(compact_shipment_bp)
app.register_blueprint(enrich_summary_bp)
app.register_blueprint(reconcile_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
