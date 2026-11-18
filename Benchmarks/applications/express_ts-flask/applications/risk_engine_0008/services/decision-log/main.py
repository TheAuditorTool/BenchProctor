import os
from flask import Flask

from decision_record import bp as decision_record_bp
from render_rule import bp as render_rule_bp
from publish_report import bp as publish_report_bp
from audit_threshold import bp as audit_threshold_bp
from merge_roster import bp as merge_roster_bp
from verify_profile import bp as verify_profile_bp
from merge_digest import bp as merge_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(decision_record_bp)
app.register_blueprint(render_rule_bp)
app.register_blueprint(publish_report_bp)
app.register_blueprint(audit_threshold_bp)
app.register_blueprint(merge_roster_bp)
app.register_blueprint(verify_profile_bp)
app.register_blueprint(merge_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
