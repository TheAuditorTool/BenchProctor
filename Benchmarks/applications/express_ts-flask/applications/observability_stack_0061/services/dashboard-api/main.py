import os
from flask import Flask

from dashboard_query import bp as dashboard_query_bp
from build_threshold import bp as build_threshold_bp
from enrich_policy import bp as enrich_policy_bp
from summarize_report import bp as summarize_report_bp
from summarize_roster import bp as summarize_roster_bp
from format_schedule import bp as format_schedule_bp
from publish_header import bp as publish_header_bp
from format_bundle import bp as format_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(dashboard_query_bp)
app.register_blueprint(build_threshold_bp)
app.register_blueprint(enrich_policy_bp)
app.register_blueprint(summarize_report_bp)
app.register_blueprint(summarize_roster_bp)
app.register_blueprint(format_schedule_bp)
app.register_blueprint(publish_header_bp)
app.register_blueprint(format_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
