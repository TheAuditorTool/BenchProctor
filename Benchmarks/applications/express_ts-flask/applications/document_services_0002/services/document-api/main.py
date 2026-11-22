import os
from flask import Flask

from document_upload import bp as document_upload_bp
from audit_batch import bp as audit_batch_bp
from load_receipt import bp as load_receipt_bp
from reconcile_threshold import bp as reconcile_threshold_bp
from audit_record import bp as audit_record_bp
from enrich_manifest import bp as enrich_manifest_bp
from build_signature import bp as build_signature_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(document_upload_bp)
app.register_blueprint(audit_batch_bp)
app.register_blueprint(load_receipt_bp)
app.register_blueprint(reconcile_threshold_bp)
app.register_blueprint(audit_record_bp)
app.register_blueprint(enrich_manifest_bp)
app.register_blueprint(build_signature_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
