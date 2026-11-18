import os
from flask import Flask

from tenant_provision import bp as tenant_provision_bp
from reconcile_checkpoint import bp as reconcile_checkpoint_bp
from annotate_schedule import bp as annotate_schedule_bp
from collect_digest import bp as collect_digest_bp
from build_config import bp as build_config_bp
from prune_record import bp as prune_record_bp
from audit_manifest import bp as audit_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(tenant_provision_bp)
app.register_blueprint(reconcile_checkpoint_bp)
app.register_blueprint(annotate_schedule_bp)
app.register_blueprint(collect_digest_bp)
app.register_blueprint(build_config_bp)
app.register_blueprint(prune_record_bp)
app.register_blueprint(audit_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
