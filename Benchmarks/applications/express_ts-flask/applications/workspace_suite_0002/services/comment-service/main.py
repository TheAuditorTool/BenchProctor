import os
from flask import Flask

from comment_post import bp as comment_post_bp
from load_snapshot import bp as load_snapshot_bp
from validate_config import bp as validate_config_bp
from load_digest import bp as load_digest_bp
from reconcile_snapshot import bp as reconcile_snapshot_bp
from export_policy import bp as export_policy_bp
from fetch_comment import bp as fetch_comment_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(comment_post_bp)
app.register_blueprint(load_snapshot_bp)
app.register_blueprint(validate_config_bp)
app.register_blueprint(load_digest_bp)
app.register_blueprint(reconcile_snapshot_bp)
app.register_blueprint(export_policy_bp)
app.register_blueprint(fetch_comment_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
