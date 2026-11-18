import os
from flask import Flask

from escalation_raise import bp as escalation_raise_bp
from load_threshold import bp as load_threshold_bp
from audit_header import bp as audit_header_bp
from audit_escalation import bp as audit_escalation_bp
from validate_checkpoint import bp as validate_checkpoint_bp
from merge_ticket import bp as merge_ticket_bp
from build_header import bp as build_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(escalation_raise_bp)
app.register_blueprint(load_threshold_bp)
app.register_blueprint(audit_header_bp)
app.register_blueprint(audit_escalation_bp)
app.register_blueprint(validate_checkpoint_bp)
app.register_blueprint(merge_ticket_bp)
app.register_blueprint(build_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
