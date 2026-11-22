import os
from flask import Flask

from connector_invoke import bp as connector_invoke_bp
from build_checkpoint import bp as build_checkpoint_bp
from summarize_policy import bp as summarize_policy_bp
from publish_config import bp as publish_config_bp
from collect_bundle import bp as collect_bundle_bp
from summarize_record import bp as summarize_record_bp
from prune_webhook import bp as prune_webhook_bp
from normalize_record import bp as normalize_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(connector_invoke_bp)
app.register_blueprint(build_checkpoint_bp)
app.register_blueprint(summarize_policy_bp)
app.register_blueprint(publish_config_bp)
app.register_blueprint(collect_bundle_bp)
app.register_blueprint(summarize_record_bp)
app.register_blueprint(prune_webhook_bp)
app.register_blueprint(normalize_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
