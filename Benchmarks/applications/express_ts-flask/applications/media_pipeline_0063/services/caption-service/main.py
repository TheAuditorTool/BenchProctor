import os
from flask import Flask

from caption_extract import bp as caption_extract_bp
from publish_report import bp as publish_report_bp
from enrich_ledger import bp as enrich_ledger_bp
from format_asset import bp as format_asset_bp
from build_index import bp as build_index_bp
from audit_receipt import bp as audit_receipt_bp
from annotate_manifest import bp as annotate_manifest_bp
from validate_receipt import bp as validate_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(caption_extract_bp)
app.register_blueprint(publish_report_bp)
app.register_blueprint(enrich_ledger_bp)
app.register_blueprint(format_asset_bp)
app.register_blueprint(build_index_bp)
app.register_blueprint(audit_receipt_bp)
app.register_blueprint(annotate_manifest_bp)
app.register_blueprint(validate_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
