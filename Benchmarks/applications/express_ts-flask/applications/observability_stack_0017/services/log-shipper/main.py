import os
from flask import Flask

from log_ship import bp as log_ship_bp
from resolve_ledger import bp as resolve_ledger_bp
from normalize_policy import bp as normalize_policy_bp
from resolve_snapshot import bp as resolve_snapshot_bp
from load_record import bp as load_record_bp
from compact_config import bp as compact_config_bp
from render_policy import bp as render_policy_bp
from reconcile_header import bp as reconcile_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(log_ship_bp)
app.register_blueprint(resolve_ledger_bp)
app.register_blueprint(normalize_policy_bp)
app.register_blueprint(resolve_snapshot_bp)
app.register_blueprint(load_record_bp)
app.register_blueprint(compact_config_bp)
app.register_blueprint(render_policy_bp)
app.register_blueprint(reconcile_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
