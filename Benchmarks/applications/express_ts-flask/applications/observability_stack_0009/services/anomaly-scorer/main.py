import os
from flask import Flask

from anomaly_score import bp as anomaly_score_bp
from build_policy import bp as build_policy_bp
from reconcile_roster import bp as reconcile_roster_bp
from compact_digest import bp as compact_digest_bp
from fetch_trace import bp as fetch_trace_bp
from reconcile_bundle import bp as reconcile_bundle_bp
from format_digest import bp as format_digest_bp
from audit_config import bp as audit_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(anomaly_score_bp)
app.register_blueprint(build_policy_bp)
app.register_blueprint(reconcile_roster_bp)
app.register_blueprint(compact_digest_bp)
app.register_blueprint(fetch_trace_bp)
app.register_blueprint(reconcile_bundle_bp)
app.register_blueprint(format_digest_bp)
app.register_blueprint(audit_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
