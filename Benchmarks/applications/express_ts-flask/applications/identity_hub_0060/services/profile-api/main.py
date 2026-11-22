import os
from flask import Flask

from profile_update import bp as profile_update_bp
from format_snapshot import bp as format_snapshot_bp
from build_report import bp as build_report_bp
from audit_device import bp as audit_device_bp
from merge_receipt import bp as merge_receipt_bp
from verify_window import bp as verify_window_bp
from normalize_profile import bp as normalize_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(profile_update_bp)
app.register_blueprint(format_snapshot_bp)
app.register_blueprint(build_report_bp)
app.register_blueprint(audit_device_bp)
app.register_blueprint(merge_receipt_bp)
app.register_blueprint(verify_window_bp)
app.register_blueprint(normalize_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
