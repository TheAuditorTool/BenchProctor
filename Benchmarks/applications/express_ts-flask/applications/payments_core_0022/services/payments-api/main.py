import os
from flask import Flask

from payment_authorize import bp as payment_authorize_bp
from annotate_snapshot import bp as annotate_snapshot_bp
from enrich_schedule import bp as enrich_schedule_bp
from archive_policy import bp as archive_policy_bp
from audit_threshold import bp as audit_threshold_bp
from summarize_threshold import bp as summarize_threshold_bp
from fetch_record import bp as fetch_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_authorize_bp)
app.register_blueprint(annotate_snapshot_bp)
app.register_blueprint(enrich_schedule_bp)
app.register_blueprint(archive_policy_bp)
app.register_blueprint(audit_threshold_bp)
app.register_blueprint(summarize_threshold_bp)
app.register_blueprint(fetch_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
