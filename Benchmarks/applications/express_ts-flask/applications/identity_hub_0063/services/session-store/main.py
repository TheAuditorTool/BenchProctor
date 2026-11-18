import os
from flask import Flask

from session_create import bp as session_create_bp
from annotate_snapshot import bp as annotate_snapshot_bp
from compact_digest import bp as compact_digest_bp
from audit_summary import bp as audit_summary_bp
from render_ledger import bp as render_ledger_bp
from format_checkpoint import bp as format_checkpoint_bp
from enrich_session import bp as enrich_session_bp
from enrich_receipt import bp as enrich_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(session_create_bp)
app.register_blueprint(annotate_snapshot_bp)
app.register_blueprint(compact_digest_bp)
app.register_blueprint(audit_summary_bp)
app.register_blueprint(render_ledger_bp)
app.register_blueprint(format_checkpoint_bp)
app.register_blueprint(enrich_session_bp)
app.register_blueprint(enrich_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
