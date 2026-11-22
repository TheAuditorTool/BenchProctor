import os
from flask import Flask

from preview_render import bp as preview_render_bp
from enrich_bundle import bp as enrich_bundle_bp
from build_snapshot import bp as build_snapshot_bp
from export_roster import bp as export_roster_bp
from enrich_report import bp as enrich_report_bp
from summarize_summary import bp as summarize_summary_bp
from annotate_threshold import bp as annotate_threshold_bp
from rotate_checkpoint import bp as rotate_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(preview_render_bp)
app.register_blueprint(enrich_bundle_bp)
app.register_blueprint(build_snapshot_bp)
app.register_blueprint(export_roster_bp)
app.register_blueprint(enrich_report_bp)
app.register_blueprint(summarize_summary_bp)
app.register_blueprint(annotate_threshold_bp)
app.register_blueprint(rotate_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
