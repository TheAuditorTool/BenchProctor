import os
from flask import Flask

from presence_update import bp as presence_update_bp
from merge_manifest import bp as merge_manifest_bp
from normalize_checkpoint import bp as normalize_checkpoint_bp
from fetch_digest import bp as fetch_digest_bp
from validate_roster import bp as validate_roster_bp
from fetch_report import bp as fetch_report_bp
from validate_digest import bp as validate_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(presence_update_bp)
app.register_blueprint(merge_manifest_bp)
app.register_blueprint(normalize_checkpoint_bp)
app.register_blueprint(fetch_digest_bp)
app.register_blueprint(validate_roster_bp)
app.register_blueprint(fetch_report_bp)
app.register_blueprint(validate_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
