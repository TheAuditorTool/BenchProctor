import os
from flask import Flask

from capture_settle import bp as capture_settle_bp
from build_threshold import bp as build_threshold_bp
from summarize_manifest import bp as summarize_manifest_bp
from validate_config import bp as validate_config_bp
from publish_policy import bp as publish_policy_bp
from enrich_wallet import bp as enrich_wallet_bp
from merge_digest import bp as merge_digest_bp
from summarize_record import bp as summarize_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(capture_settle_bp)
app.register_blueprint(build_threshold_bp)
app.register_blueprint(summarize_manifest_bp)
app.register_blueprint(validate_config_bp)
app.register_blueprint(publish_policy_bp)
app.register_blueprint(enrich_wallet_bp)
app.register_blueprint(merge_digest_bp)
app.register_blueprint(summarize_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
