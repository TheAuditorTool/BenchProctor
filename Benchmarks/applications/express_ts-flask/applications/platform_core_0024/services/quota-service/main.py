import os
from flask import Flask

from quota_enforce import bp as quota_enforce_bp
from build_policy import bp as build_policy_bp
from reconcile_policy import bp as reconcile_policy_bp
from collect_threshold import bp as collect_threshold_bp
from format_schedule import bp as format_schedule_bp
from load_policy import bp as load_policy_bp
from validate_quota import bp as validate_quota_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(quota_enforce_bp)
app.register_blueprint(build_policy_bp)
app.register_blueprint(reconcile_policy_bp)
app.register_blueprint(collect_threshold_bp)
app.register_blueprint(format_schedule_bp)
app.register_blueprint(load_policy_bp)
app.register_blueprint(validate_quota_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
