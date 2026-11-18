import os
from flask import Flask

from manifest_build import bp as manifest_build_bp
from audit_header import bp as audit_header_bp
from rotate_config import bp as rotate_config_bp
from audit_report import bp as audit_report_bp
from verify_manifest import bp as verify_manifest_bp
from reconcile_threshold import bp as reconcile_threshold_bp
from verify_checkpoint import bp as verify_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(manifest_build_bp)
app.register_blueprint(audit_header_bp)
app.register_blueprint(rotate_config_bp)
app.register_blueprint(audit_report_bp)
app.register_blueprint(verify_manifest_bp)
app.register_blueprint(reconcile_threshold_bp)
app.register_blueprint(verify_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
