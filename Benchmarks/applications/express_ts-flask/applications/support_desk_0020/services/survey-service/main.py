import os
from flask import Flask

from survey_send import bp as survey_send_bp
from render_ticket import bp as render_ticket_bp
from load_bundle import bp as load_bundle_bp
from archive_config import bp as archive_config_bp
from archive_snapshot import bp as archive_snapshot_bp
from validate_window import bp as validate_window_bp
from validate_bundle import bp as validate_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(survey_send_bp)
app.register_blueprint(render_ticket_bp)
app.register_blueprint(load_bundle_bp)
app.register_blueprint(archive_config_bp)
app.register_blueprint(archive_snapshot_bp)
app.register_blueprint(validate_window_bp)
app.register_blueprint(validate_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
