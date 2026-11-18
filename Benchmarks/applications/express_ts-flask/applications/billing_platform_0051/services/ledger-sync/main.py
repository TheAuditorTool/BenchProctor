import os
from flask import Flask

from ledger_post import bp as ledger_post_bp
from validate_header import bp as validate_header_bp
from render_profile import bp as render_profile_bp
from archive_report import bp as archive_report_bp
from normalize_schedule import bp as normalize_schedule_bp
from resolve_snapshot import bp as resolve_snapshot_bp
from compact_receipt import bp as compact_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(ledger_post_bp)
app.register_blueprint(validate_header_bp)
app.register_blueprint(render_profile_bp)
app.register_blueprint(archive_report_bp)
app.register_blueprint(normalize_schedule_bp)
app.register_blueprint(resolve_snapshot_bp)
app.register_blueprint(compact_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
