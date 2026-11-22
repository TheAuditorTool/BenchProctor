import os
from flask import Flask

from session_create import bp as session_create_bp
from render_config import bp as render_config_bp
from archive_ledger import bp as archive_ledger_bp
from normalize_threshold import bp as normalize_threshold_bp
from reconcile_roster import bp as reconcile_roster_bp
from annotate_device import bp as annotate_device_bp
from summarize_batch import bp as summarize_batch_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(session_create_bp)
app.register_blueprint(render_config_bp)
app.register_blueprint(archive_ledger_bp)
app.register_blueprint(normalize_threshold_bp)
app.register_blueprint(reconcile_roster_bp)
app.register_blueprint(annotate_device_bp)
app.register_blueprint(summarize_batch_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
