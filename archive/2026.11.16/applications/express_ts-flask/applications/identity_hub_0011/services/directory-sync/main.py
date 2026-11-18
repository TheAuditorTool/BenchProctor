import os
from flask import Flask

from directory_sync import bp as directory_sync_bp
from prune_ledger import bp as prune_ledger_bp
from audit_profile import bp as audit_profile_bp
from normalize_threshold import bp as normalize_threshold_bp
from compact_config import bp as compact_config_bp
from format_batch import bp as format_batch_bp
from format_checkpoint import bp as format_checkpoint_bp
from format_receipt import bp as format_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(directory_sync_bp)
app.register_blueprint(prune_ledger_bp)
app.register_blueprint(audit_profile_bp)
app.register_blueprint(normalize_threshold_bp)
app.register_blueprint(compact_config_bp)
app.register_blueprint(format_batch_bp)
app.register_blueprint(format_checkpoint_bp)
app.register_blueprint(format_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
