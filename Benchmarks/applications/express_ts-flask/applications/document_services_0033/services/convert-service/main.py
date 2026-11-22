import os
from flask import Flask

from convert_job import bp as convert_job_bp
from audit_summary import bp as audit_summary_bp
from publish_schedule import bp as publish_schedule_bp
from enrich_receipt import bp as enrich_receipt_bp
from fetch_record import bp as fetch_record_bp
from render_threshold import bp as render_threshold_bp
from format_profile import bp as format_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(convert_job_bp)
app.register_blueprint(audit_summary_bp)
app.register_blueprint(publish_schedule_bp)
app.register_blueprint(enrich_receipt_bp)
app.register_blueprint(fetch_record_bp)
app.register_blueprint(render_threshold_bp)
app.register_blueprint(format_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
