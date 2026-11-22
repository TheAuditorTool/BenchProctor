import os
from flask import Flask

from escalation_raise import bp as escalation_raise_bp
from publish_threshold import bp as publish_threshold_bp
from load_threshold import bp as load_threshold_bp
from load_escalation import bp as load_escalation_bp
from resolve_summary import bp as resolve_summary_bp
from audit_schedule import bp as audit_schedule_bp
from audit_config import bp as audit_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(escalation_raise_bp)
app.register_blueprint(publish_threshold_bp)
app.register_blueprint(load_threshold_bp)
app.register_blueprint(load_escalation_bp)
app.register_blueprint(resolve_summary_bp)
app.register_blueprint(audit_schedule_bp)
app.register_blueprint(audit_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
