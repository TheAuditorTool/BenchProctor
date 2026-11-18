import os
from flask import Flask

from fx_convert import bp as fx_convert_bp
from compact_receipt import bp as compact_receipt_bp
from merge_snapshot import bp as merge_snapshot_bp
from normalize_dispute import bp as normalize_dispute_bp
from reconcile_config import bp as reconcile_config_bp
from format_policy import bp as format_policy_bp
from validate_receipt import bp as validate_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(fx_convert_bp)
app.register_blueprint(compact_receipt_bp)
app.register_blueprint(merge_snapshot_bp)
app.register_blueprint(normalize_dispute_bp)
app.register_blueprint(reconcile_config_bp)
app.register_blueprint(format_policy_bp)
app.register_blueprint(validate_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
