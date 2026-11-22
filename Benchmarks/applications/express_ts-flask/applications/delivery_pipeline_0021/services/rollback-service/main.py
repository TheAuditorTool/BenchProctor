import os
from flask import Flask

from rollback_trigger import bp as rollback_trigger_bp
from prune_release import bp as prune_release_bp
from build_summary import bp as build_summary_bp
from merge_canary import bp as merge_canary_bp
from normalize_config import bp as normalize_config_bp
from format_summary import bp as format_summary_bp
from export_report import bp as export_report_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(rollback_trigger_bp)
app.register_blueprint(prune_release_bp)
app.register_blueprint(build_summary_bp)
app.register_blueprint(merge_canary_bp)
app.register_blueprint(normalize_config_bp)
app.register_blueprint(format_summary_bp)
app.register_blueprint(export_report_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
