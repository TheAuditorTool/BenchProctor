import os
from flask import Flask

from retry_queue import bp as retry_queue_bp
from render_window import bp as render_window_bp
from enrich_threshold import bp as enrich_threshold_bp
from export_roster import bp as export_roster_bp
from load_bundle import bp as load_bundle_bp
from merge_config import bp as merge_config_bp
from audit_bundle import bp as audit_bundle_bp
from normalize_header import bp as normalize_header_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retry_queue_bp)
app.register_blueprint(render_window_bp)
app.register_blueprint(enrich_threshold_bp)
app.register_blueprint(export_roster_bp)
app.register_blueprint(load_bundle_bp)
app.register_blueprint(merge_config_bp)
app.register_blueprint(audit_bundle_bp)
app.register_blueprint(normalize_header_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
