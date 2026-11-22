import os
from flask import Flask

from shipment_quote import bp as shipment_quote_bp
from publish_ledger import bp as publish_ledger_bp
from verify_threshold import bp as verify_threshold_bp
from fetch_policy import bp as fetch_policy_bp
from format_report import bp as format_report_bp
from merge_batch import bp as merge_batch_bp
from build_snapshot import bp as build_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(shipment_quote_bp)
app.register_blueprint(publish_ledger_bp)
app.register_blueprint(verify_threshold_bp)
app.register_blueprint(fetch_policy_bp)
app.register_blueprint(format_report_bp)
app.register_blueprint(merge_batch_bp)
app.register_blueprint(build_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
