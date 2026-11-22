import os
from flask import Flask

from share_grant import bp as share_grant_bp
from normalize_policy import bp as normalize_policy_bp
from prune_workspace import bp as prune_workspace_bp
from reconcile_digest import bp as reconcile_digest_bp
from compact_report import bp as compact_report_bp
from merge_ledger import bp as merge_ledger_bp
from validate_comment import bp as validate_comment_bp
from normalize_record import bp as normalize_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(share_grant_bp)
app.register_blueprint(normalize_policy_bp)
app.register_blueprint(prune_workspace_bp)
app.register_blueprint(reconcile_digest_bp)
app.register_blueprint(compact_report_bp)
app.register_blueprint(merge_ledger_bp)
app.register_blueprint(validate_comment_bp)
app.register_blueprint(normalize_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
