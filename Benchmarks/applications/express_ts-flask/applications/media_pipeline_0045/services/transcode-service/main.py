import os
from flask import Flask

from transcode_job import bp as transcode_job_bp
from enrich_threshold import bp as enrich_threshold_bp
from merge_index import bp as merge_index_bp
from fetch_window import bp as fetch_window_bp
from load_policy import bp as load_policy_bp
from prune_ledger import bp as prune_ledger_bp
from format_manifest import bp as format_manifest_bp
from prune_digest import bp as prune_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(transcode_job_bp)
app.register_blueprint(enrich_threshold_bp)
app.register_blueprint(merge_index_bp)
app.register_blueprint(fetch_window_bp)
app.register_blueprint(load_policy_bp)
app.register_blueprint(prune_ledger_bp)
app.register_blueprint(format_manifest_bp)
app.register_blueprint(prune_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
