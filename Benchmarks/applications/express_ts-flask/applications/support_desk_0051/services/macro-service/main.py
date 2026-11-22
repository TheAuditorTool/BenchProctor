import os
from flask import Flask

from macro_apply import bp as macro_apply_bp
from audit_threshold import bp as audit_threshold_bp
from normalize_profile import bp as normalize_profile_bp
from reconcile_index import bp as reconcile_index_bp
from resolve_index import bp as resolve_index_bp
from audit_bundle import bp as audit_bundle_bp
from enrich_config import bp as enrich_config_bp
from validate_snapshot import bp as validate_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(macro_apply_bp)
app.register_blueprint(audit_threshold_bp)
app.register_blueprint(normalize_profile_bp)
app.register_blueprint(reconcile_index_bp)
app.register_blueprint(resolve_index_bp)
app.register_blueprint(audit_bundle_bp)
app.register_blueprint(enrich_config_bp)
app.register_blueprint(validate_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
