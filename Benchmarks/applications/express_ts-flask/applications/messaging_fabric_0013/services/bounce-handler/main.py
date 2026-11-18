import os
from flask import Flask

from bounce_record import bp as bounce_record_bp
from compact_ledger import bp as compact_ledger_bp
from format_batch import bp as format_batch_bp
from verify_window import bp as verify_window_bp
from annotate_delivery import bp as annotate_delivery_bp
from resolve_digest import bp as resolve_digest_bp
from validate_snapshot import bp as validate_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(bounce_record_bp)
app.register_blueprint(compact_ledger_bp)
app.register_blueprint(format_batch_bp)
app.register_blueprint(verify_window_bp)
app.register_blueprint(annotate_delivery_bp)
app.register_blueprint(resolve_digest_bp)
app.register_blueprint(validate_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
