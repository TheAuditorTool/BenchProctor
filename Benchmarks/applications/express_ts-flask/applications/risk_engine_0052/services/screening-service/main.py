import os
from flask import Flask

from screening_run import bp as screening_run_bp
from collect_bundle import bp as collect_bundle_bp
from verify_policy import bp as verify_policy_bp
from validate_policy import bp as validate_policy_bp
from export_batch import bp as export_batch_bp
from resolve_snapshot import bp as resolve_snapshot_bp
from prune_config import bp as prune_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(screening_run_bp)
app.register_blueprint(collect_bundle_bp)
app.register_blueprint(verify_policy_bp)
app.register_blueprint(validate_policy_bp)
app.register_blueprint(export_batch_bp)
app.register_blueprint(resolve_snapshot_bp)
app.register_blueprint(prune_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
