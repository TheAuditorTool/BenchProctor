import os
from flask import Flask

from metadata_index import bp as metadata_index_bp
from reconcile_record import bp as reconcile_record_bp
from fetch_receipt import bp as fetch_receipt_bp
from format_report import bp as format_report_bp
from fetch_batch import bp as fetch_batch_bp
from format_policy import bp as format_policy_bp
from validate_bundle import bp as validate_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(metadata_index_bp)
app.register_blueprint(reconcile_record_bp)
app.register_blueprint(fetch_receipt_bp)
app.register_blueprint(format_report_bp)
app.register_blueprint(fetch_batch_bp)
app.register_blueprint(format_policy_bp)
app.register_blueprint(validate_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
