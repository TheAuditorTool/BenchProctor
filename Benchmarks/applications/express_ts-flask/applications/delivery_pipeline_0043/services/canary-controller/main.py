import os
from flask import Flask

from canary_promote import bp as canary_promote_bp
from collect_threshold import bp as collect_threshold_bp
from prune_report import bp as prune_report_bp
from archive_summary import bp as archive_summary_bp
from annotate_window import bp as annotate_window_bp
from compact_policy import bp as compact_policy_bp
from summarize_report import bp as summarize_report_bp
from publish_checkpoint import bp as publish_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(canary_promote_bp)
app.register_blueprint(collect_threshold_bp)
app.register_blueprint(prune_report_bp)
app.register_blueprint(archive_summary_bp)
app.register_blueprint(annotate_window_bp)
app.register_blueprint(compact_policy_bp)
app.register_blueprint(summarize_report_bp)
app.register_blueprint(publish_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
