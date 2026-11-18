import os
from flask import Flask

from label_create import bp as label_create_bp
from verify_profile import bp as verify_profile_bp
from publish_receipt import bp as publish_receipt_bp
from reconcile_checkpoint import bp as reconcile_checkpoint_bp
from validate_profile import bp as validate_profile_bp
from build_header import bp as build_header_bp
from archive_threshold import bp as archive_threshold_bp
from resolve_summary import bp as resolve_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(label_create_bp)
app.register_blueprint(verify_profile_bp)
app.register_blueprint(publish_receipt_bp)
app.register_blueprint(reconcile_checkpoint_bp)
app.register_blueprint(validate_profile_bp)
app.register_blueprint(build_header_bp)
app.register_blueprint(archive_threshold_bp)
app.register_blueprint(resolve_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
