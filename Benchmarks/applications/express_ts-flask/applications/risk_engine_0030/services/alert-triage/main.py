import os
from flask import Flask

from alert_triage import bp as alert_triage_bp
from enrich_schedule import bp as enrich_schedule_bp
from compact_roster import bp as compact_roster_bp
from build_decision import bp as build_decision_bp
from reconcile_batch import bp as reconcile_batch_bp
from archive_schedule import bp as archive_schedule_bp
from archive_rule import bp as archive_rule_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(alert_triage_bp)
app.register_blueprint(enrich_schedule_bp)
app.register_blueprint(compact_roster_bp)
app.register_blueprint(build_decision_bp)
app.register_blueprint(reconcile_batch_bp)
app.register_blueprint(archive_schedule_bp)
app.register_blueprint(archive_rule_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
