import os
from flask import Flask

from payment_capture import bp as payment_capture_bp
from compact_policy import bp as compact_policy_bp
from prune_summary import bp as prune_summary_bp
from normalize_invoice import bp as normalize_invoice_bp
from enrich_manifest import bp as enrich_manifest_bp
from validate_summary import bp as validate_summary_bp
from collect_header import bp as collect_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_capture_bp)
app.register_blueprint(compact_policy_bp)
app.register_blueprint(prune_summary_bp)
app.register_blueprint(normalize_invoice_bp)
app.register_blueprint(enrich_manifest_bp)
app.register_blueprint(validate_summary_bp)
app.register_blueprint(collect_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
