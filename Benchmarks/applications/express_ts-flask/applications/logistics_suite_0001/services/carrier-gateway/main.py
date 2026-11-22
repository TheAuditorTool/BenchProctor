import os
from flask import Flask

from carrier_dispatch import bp as carrier_dispatch_bp
from fetch_profile import bp as fetch_profile_bp
from validate_digest import bp as validate_digest_bp
from export_summary import bp as export_summary_bp
from fetch_digest import bp as fetch_digest_bp
from export_receipt import bp as export_receipt_bp
from prune_checkpoint import bp as prune_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(carrier_dispatch_bp)
app.register_blueprint(fetch_profile_bp)
app.register_blueprint(validate_digest_bp)
app.register_blueprint(export_summary_bp)
app.register_blueprint(fetch_digest_bp)
app.register_blueprint(export_receipt_bp)
app.register_blueprint(prune_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
