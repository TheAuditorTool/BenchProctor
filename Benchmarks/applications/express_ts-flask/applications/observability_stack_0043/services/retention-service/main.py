import os
from flask import Flask

from retention_sweep import bp as retention_sweep_bp
from summarize_alert import bp as summarize_alert_bp
from export_roster import bp as export_roster_bp
from verify_threshold import bp as verify_threshold_bp
from validate_record import bp as validate_record_bp
from prune_checkpoint import bp as prune_checkpoint_bp
from export_header import bp as export_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retention_sweep_bp)
app.register_blueprint(summarize_alert_bp)
app.register_blueprint(export_roster_bp)
app.register_blueprint(verify_threshold_bp)
app.register_blueprint(validate_record_bp)
app.register_blueprint(prune_checkpoint_bp)
app.register_blueprint(export_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
