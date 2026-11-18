import os
from flask import Flask

from payment_capture import bp as payment_capture_bp
from render_batch import bp as render_batch_bp
from build_summary import bp as build_summary_bp
from render_snapshot import bp as render_snapshot_bp
from annotate_policy import bp as annotate_policy_bp
from render_invoice import bp as render_invoice_bp
from build_ledger import bp as build_ledger_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_capture_bp)
app.register_blueprint(render_batch_bp)
app.register_blueprint(build_summary_bp)
app.register_blueprint(render_snapshot_bp)
app.register_blueprint(annotate_policy_bp)
app.register_blueprint(render_invoice_bp)
app.register_blueprint(build_ledger_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
