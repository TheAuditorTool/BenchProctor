import os
from flask import Flask

from settlement_batch import bp as settlement_batch_bp
from resolve_snapshot import bp as resolve_snapshot_bp
from compact_receipt import bp as compact_receipt_bp
from rotate_report import bp as rotate_report_bp
from prune_report import bp as prune_report_bp
from validate_schedule import bp as validate_schedule_bp
from fetch_schedule import bp as fetch_schedule_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(settlement_batch_bp)
app.register_blueprint(resolve_snapshot_bp)
app.register_blueprint(compact_receipt_bp)
app.register_blueprint(rotate_report_bp)
app.register_blueprint(prune_report_bp)
app.register_blueprint(validate_schedule_bp)
app.register_blueprint(fetch_schedule_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
