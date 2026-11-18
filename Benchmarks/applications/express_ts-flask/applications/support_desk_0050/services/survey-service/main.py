import os
from flask import Flask

from survey_send import bp as survey_send_bp
from enrich_policy import bp as enrich_policy_bp
from audit_snapshot import bp as audit_snapshot_bp
from compact_record import bp as compact_record_bp
from merge_bundle import bp as merge_bundle_bp
from prune_manifest import bp as prune_manifest_bp
from fetch_header import bp as fetch_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(survey_send_bp)
app.register_blueprint(enrich_policy_bp)
app.register_blueprint(audit_snapshot_bp)
app.register_blueprint(compact_record_bp)
app.register_blueprint(merge_bundle_bp)
app.register_blueprint(prune_manifest_bp)
app.register_blueprint(fetch_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
