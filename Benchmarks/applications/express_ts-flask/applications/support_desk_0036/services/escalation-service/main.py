import os
from flask import Flask

from escalation_raise import bp as escalation_raise_bp
from validate_manifest import bp as validate_manifest_bp
from collect_policy import bp as collect_policy_bp
from resolve_header import bp as resolve_header_bp
from publish_batch import bp as publish_batch_bp
from collect_checkpoint import bp as collect_checkpoint_bp
from enrich_batch import bp as enrich_batch_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(escalation_raise_bp)
app.register_blueprint(validate_manifest_bp)
app.register_blueprint(collect_policy_bp)
app.register_blueprint(resolve_header_bp)
app.register_blueprint(publish_batch_bp)
app.register_blueprint(collect_checkpoint_bp)
app.register_blueprint(enrich_batch_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
