import os
from flask import Flask

from consent_record import bp as consent_record_bp
from merge_policy import bp as merge_policy_bp
from prune_policy import bp as prune_policy_bp
from audit_digest import bp as audit_digest_bp
from validate_manifest import bp as validate_manifest_bp
from summarize_schedule import bp as summarize_schedule_bp
from enrich_config import bp as enrich_config_bp
from collect_snapshot import bp as collect_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(consent_record_bp)
app.register_blueprint(merge_policy_bp)
app.register_blueprint(prune_policy_bp)
app.register_blueprint(audit_digest_bp)
app.register_blueprint(validate_manifest_bp)
app.register_blueprint(summarize_schedule_bp)
app.register_blueprint(enrich_config_bp)
app.register_blueprint(collect_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
