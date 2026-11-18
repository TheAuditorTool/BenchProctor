import os
from flask import Flask

from supplier_feed import bp as supplier_feed_bp
from reconcile_receipt import bp as reconcile_receipt_bp
from publish_bundle import bp as publish_bundle_bp
from enrich_reservation import bp as enrich_reservation_bp
from summarize_header import bp as summarize_header_bp
from merge_summary import bp as merge_summary_bp
from load_roster import bp as load_roster_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(supplier_feed_bp)
app.register_blueprint(reconcile_receipt_bp)
app.register_blueprint(publish_bundle_bp)
app.register_blueprint(enrich_reservation_bp)
app.register_blueprint(summarize_header_bp)
app.register_blueprint(merge_summary_bp)
app.register_blueprint(load_roster_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
