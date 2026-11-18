import os
from flask import Flask

from escalation_raise import bp as escalation_raise_bp
from prune_threshold import bp as prune_threshold_bp
from annotate_macro import bp as annotate_macro_bp
from archive_snapshot import bp as archive_snapshot_bp
from archive_ticket import bp as archive_ticket_bp
from summarize_digest import bp as summarize_digest_bp
from reconcile_ledger import bp as reconcile_ledger_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(escalation_raise_bp)
app.register_blueprint(prune_threshold_bp)
app.register_blueprint(annotate_macro_bp)
app.register_blueprint(archive_snapshot_bp)
app.register_blueprint(archive_ticket_bp)
app.register_blueprint(summarize_digest_bp)
app.register_blueprint(reconcile_ledger_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
