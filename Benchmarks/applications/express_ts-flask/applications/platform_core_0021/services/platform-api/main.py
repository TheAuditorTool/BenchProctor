import os
from flask import Flask

from tenant_provision import bp as tenant_provision_bp
from audit_threshold import bp as audit_threshold_bp
from merge_policy import bp as merge_policy_bp
from archive_config import bp as archive_config_bp
from rotate_bundle import bp as rotate_bundle_bp
from audit_header import bp as audit_header_bp
from verify_receipt import bp as verify_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(tenant_provision_bp)
app.register_blueprint(audit_threshold_bp)
app.register_blueprint(merge_policy_bp)
app.register_blueprint(archive_config_bp)
app.register_blueprint(rotate_bundle_bp)
app.register_blueprint(audit_header_bp)
app.register_blueprint(verify_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
