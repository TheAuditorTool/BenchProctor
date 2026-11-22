import os
from flask import Flask

from dashboard_query import bp as dashboard_query_bp
from validate_profile import bp as validate_profile_bp
from enrich_report import bp as enrich_report_bp
from annotate_receipt import bp as annotate_receipt_bp
from fetch_snapshot import bp as fetch_snapshot_bp
from summarize_window import bp as summarize_window_bp
from fetch_sample import bp as fetch_sample_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(dashboard_query_bp)
app.register_blueprint(validate_profile_bp)
app.register_blueprint(enrich_report_bp)
app.register_blueprint(annotate_receipt_bp)
app.register_blueprint(fetch_snapshot_bp)
app.register_blueprint(summarize_window_bp)
app.register_blueprint(fetch_sample_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
