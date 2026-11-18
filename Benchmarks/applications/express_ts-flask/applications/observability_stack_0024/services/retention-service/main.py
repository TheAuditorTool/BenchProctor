import os
from flask import Flask

from retention_sweep import bp as retention_sweep_bp
from load_window import bp as load_window_bp
from reconcile_report import bp as reconcile_report_bp
from enrich_window import bp as enrich_window_bp
from rotate_digest import bp as rotate_digest_bp
from export_summary import bp as export_summary_bp
from audit_bundle import bp as audit_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retention_sweep_bp)
app.register_blueprint(load_window_bp)
app.register_blueprint(reconcile_report_bp)
app.register_blueprint(enrich_window_bp)
app.register_blueprint(rotate_digest_bp)
app.register_blueprint(export_summary_bp)
app.register_blueprint(audit_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
