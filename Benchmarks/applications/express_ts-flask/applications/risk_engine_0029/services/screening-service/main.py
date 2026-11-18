import os
from flask import Flask

from screening_run import bp as screening_run_bp
from validate_receipt import bp as validate_receipt_bp
from fetch_window import bp as fetch_window_bp
from archive_ledger import bp as archive_ledger_bp
from prune_summary import bp as prune_summary_bp
from render_header import bp as render_header_bp
from compact_digest import bp as compact_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(screening_run_bp)
app.register_blueprint(validate_receipt_bp)
app.register_blueprint(fetch_window_bp)
app.register_blueprint(archive_ledger_bp)
app.register_blueprint(prune_summary_bp)
app.register_blueprint(render_header_bp)
app.register_blueprint(compact_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
