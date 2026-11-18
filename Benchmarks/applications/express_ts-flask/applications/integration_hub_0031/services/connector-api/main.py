import os
from flask import Flask

from connector_invoke import bp as connector_invoke_bp
from validate_webhook import bp as validate_webhook_bp
from format_header import bp as format_header_bp
from reconcile_snapshot import bp as reconcile_snapshot_bp
from export_window import bp as export_window_bp
from export_policy import bp as export_policy_bp
from summarize_batch import bp as summarize_batch_bp
from render_config import bp as render_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(connector_invoke_bp)
app.register_blueprint(validate_webhook_bp)
app.register_blueprint(format_header_bp)
app.register_blueprint(reconcile_snapshot_bp)
app.register_blueprint(export_window_bp)
app.register_blueprint(export_policy_bp)
app.register_blueprint(summarize_batch_bp)
app.register_blueprint(render_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
