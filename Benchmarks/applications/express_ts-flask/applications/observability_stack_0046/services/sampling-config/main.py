import os
from flask import Flask

from sample_config import bp as sample_config_bp
from audit_bundle import bp as audit_bundle_bp
from collect_checkpoint import bp as collect_checkpoint_bp
from render_schedule import bp as render_schedule_bp
from load_metric import bp as load_metric_bp
from enrich_roster import bp as enrich_roster_bp
from export_header import bp as export_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(sample_config_bp)
app.register_blueprint(audit_bundle_bp)
app.register_blueprint(collect_checkpoint_bp)
app.register_blueprint(render_schedule_bp)
app.register_blueprint(load_metric_bp)
app.register_blueprint(enrich_roster_bp)
app.register_blueprint(export_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
