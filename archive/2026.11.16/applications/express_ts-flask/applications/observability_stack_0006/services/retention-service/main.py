import os
from flask import Flask

from retention_sweep import bp as retention_sweep_bp
from publish_sample import bp as publish_sample_bp
from annotate_schedule import bp as annotate_schedule_bp
from prune_metric import bp as prune_metric_bp
from normalize_manifest import bp as normalize_manifest_bp
from rotate_ledger import bp as rotate_ledger_bp
from load_manifest import bp as load_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retention_sweep_bp)
app.register_blueprint(publish_sample_bp)
app.register_blueprint(annotate_schedule_bp)
app.register_blueprint(prune_metric_bp)
app.register_blueprint(normalize_manifest_bp)
app.register_blueprint(rotate_ledger_bp)
app.register_blueprint(load_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
