import os
from flask import Flask

from sample_config import bp as sample_config_bp
from summarize_schedule import bp as summarize_schedule_bp
from merge_digest import bp as merge_digest_bp
from archive_manifest import bp as archive_manifest_bp
from prune_record import bp as prune_record_bp
from compact_metric import bp as compact_metric_bp
from format_roster import bp as format_roster_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(sample_config_bp)
app.register_blueprint(summarize_schedule_bp)
app.register_blueprint(merge_digest_bp)
app.register_blueprint(archive_manifest_bp)
app.register_blueprint(prune_record_bp)
app.register_blueprint(compact_metric_bp)
app.register_blueprint(format_roster_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
