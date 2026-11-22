import os
from flask import Flask

from cart_update import bp as cart_update_bp
from rotate_profile import bp as rotate_profile_bp
from format_report import bp as format_report_bp
from validate_fulfillment import bp as validate_fulfillment_bp
from publish_policy import bp as publish_policy_bp
from prune_config import bp as prune_config_bp
from summarize_checkpoint import bp as summarize_checkpoint_bp
from fetch_summary import bp as fetch_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(cart_update_bp)
app.register_blueprint(rotate_profile_bp)
app.register_blueprint(format_report_bp)
app.register_blueprint(validate_fulfillment_bp)
app.register_blueprint(publish_policy_bp)
app.register_blueprint(prune_config_bp)
app.register_blueprint(summarize_checkpoint_bp)
app.register_blueprint(fetch_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
