import os
from flask import Flask

from convert_job import bp as convert_job_bp
from publish_receipt import bp as publish_receipt_bp
from validate_manifest import bp as validate_manifest_bp
from reconcile_profile import bp as reconcile_profile_bp
from format_summary import bp as format_summary_bp
from merge_digest import bp as merge_digest_bp
from publish_manifest import bp as publish_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(convert_job_bp)
app.register_blueprint(publish_receipt_bp)
app.register_blueprint(validate_manifest_bp)
app.register_blueprint(reconcile_profile_bp)
app.register_blueprint(format_summary_bp)
app.register_blueprint(merge_digest_bp)
app.register_blueprint(publish_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
