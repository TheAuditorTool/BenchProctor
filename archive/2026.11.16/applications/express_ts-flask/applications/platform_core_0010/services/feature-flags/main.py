import os
from flask import Flask

from flag_evaluate import bp as flag_evaluate_bp
from render_snapshot import bp as render_snapshot_bp
from normalize_receipt import bp as normalize_receipt_bp
from publish_config import bp as publish_config_bp
from resolve_ledger import bp as resolve_ledger_bp
from merge_window import bp as merge_window_bp
from audit_quota import bp as audit_quota_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(flag_evaluate_bp)
app.register_blueprint(render_snapshot_bp)
app.register_blueprint(normalize_receipt_bp)
app.register_blueprint(publish_config_bp)
app.register_blueprint(resolve_ledger_bp)
app.register_blueprint(merge_window_bp)
app.register_blueprint(audit_quota_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
