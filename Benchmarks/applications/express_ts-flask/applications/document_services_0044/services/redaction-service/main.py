import os
from flask import Flask

from redaction_apply import bp as redaction_apply_bp
from rotate_bundle import bp as rotate_bundle_bp
from publish_threshold import bp as publish_threshold_bp
from normalize_report import bp as normalize_report_bp
from verify_snapshot import bp as verify_snapshot_bp
from validate_index import bp as validate_index_bp
from reconcile_threshold import bp as reconcile_threshold_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(redaction_apply_bp)
app.register_blueprint(rotate_bundle_bp)
app.register_blueprint(publish_threshold_bp)
app.register_blueprint(normalize_report_bp)
app.register_blueprint(verify_snapshot_bp)
app.register_blueprint(validate_index_bp)
app.register_blueprint(reconcile_threshold_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
