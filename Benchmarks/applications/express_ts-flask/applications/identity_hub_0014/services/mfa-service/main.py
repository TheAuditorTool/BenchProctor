import os
from flask import Flask

from mfa_verify import bp as mfa_verify_bp
from verify_config import bp as verify_config_bp
from resolve_bundle import bp as resolve_bundle_bp
from load_record import bp as load_record_bp
from collect_receipt import bp as collect_receipt_bp
from archive_checkpoint import bp as archive_checkpoint_bp
from load_digest import bp as load_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(mfa_verify_bp)
app.register_blueprint(verify_config_bp)
app.register_blueprint(resolve_bundle_bp)
app.register_blueprint(load_record_bp)
app.register_blueprint(collect_receipt_bp)
app.register_blueprint(archive_checkpoint_bp)
app.register_blueprint(load_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
