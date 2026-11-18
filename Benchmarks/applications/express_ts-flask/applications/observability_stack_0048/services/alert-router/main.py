import os
from flask import Flask

from alert_route import bp as alert_route_bp
from audit_digest import bp as audit_digest_bp
from rotate_checkpoint import bp as rotate_checkpoint_bp
from compact_receipt import bp as compact_receipt_bp
from reconcile_sample import bp as reconcile_sample_bp
from export_schedule import bp as export_schedule_bp
from build_snapshot import bp as build_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(alert_route_bp)
app.register_blueprint(audit_digest_bp)
app.register_blueprint(rotate_checkpoint_bp)
app.register_blueprint(compact_receipt_bp)
app.register_blueprint(reconcile_sample_bp)
app.register_blueprint(export_schedule_bp)
app.register_blueprint(build_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
