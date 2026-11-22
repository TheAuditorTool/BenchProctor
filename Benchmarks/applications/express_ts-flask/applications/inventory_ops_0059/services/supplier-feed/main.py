import os
from flask import Flask

from supplier_feed import bp as supplier_feed_bp
from archive_snapshot import bp as archive_snapshot_bp
from prune_header import bp as prune_header_bp
from validate_window import bp as validate_window_bp
from fetch_ledger import bp as fetch_ledger_bp
from verify_digest import bp as verify_digest_bp
from resolve_snapshot import bp as resolve_snapshot_bp
from format_policy import bp as format_policy_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(supplier_feed_bp)
app.register_blueprint(archive_snapshot_bp)
app.register_blueprint(prune_header_bp)
app.register_blueprint(validate_window_bp)
app.register_blueprint(fetch_ledger_bp)
app.register_blueprint(verify_digest_bp)
app.register_blueprint(resolve_snapshot_bp)
app.register_blueprint(format_policy_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
