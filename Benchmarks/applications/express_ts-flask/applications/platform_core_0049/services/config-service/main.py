import os
from flask import Flask

from config_rollout import bp as config_rollout_bp
from prune_digest import bp as prune_digest_bp
from rotate_batch import bp as rotate_batch_bp
from resolve_config import bp as resolve_config_bp
from resolve_batch import bp as resolve_batch_bp
from verify_checkpoint import bp as verify_checkpoint_bp
from summarize_index import bp as summarize_index_bp
from verify_bundle import bp as verify_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(config_rollout_bp)
app.register_blueprint(prune_digest_bp)
app.register_blueprint(rotate_batch_bp)
app.register_blueprint(resolve_config_bp)
app.register_blueprint(resolve_batch_bp)
app.register_blueprint(verify_checkpoint_bp)
app.register_blueprint(summarize_index_bp)
app.register_blueprint(verify_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
