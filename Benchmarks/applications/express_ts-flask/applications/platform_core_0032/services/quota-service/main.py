import os
from flask import Flask

from quota_enforce import bp as quota_enforce_bp
from archive_summary import bp as archive_summary_bp
from collect_header import bp as collect_header_bp
from publish_threshold import bp as publish_threshold_bp
from export_schedule import bp as export_schedule_bp
from summarize_window import bp as summarize_window_bp
from audit_secret import bp as audit_secret_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(quota_enforce_bp)
app.register_blueprint(archive_summary_bp)
app.register_blueprint(collect_header_bp)
app.register_blueprint(publish_threshold_bp)
app.register_blueprint(export_schedule_bp)
app.register_blueprint(summarize_window_bp)
app.register_blueprint(audit_secret_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
