import os
from flask import Flask

from rollback_trigger import bp as rollback_trigger_bp
from load_roster import bp as load_roster_bp
from summarize_release import bp as summarize_release_bp
from verify_receipt import bp as verify_receipt_bp
from export_artifact import bp as export_artifact_bp
from verify_checkpoint import bp as verify_checkpoint_bp
from fetch_roster import bp as fetch_roster_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(rollback_trigger_bp)
app.register_blueprint(load_roster_bp)
app.register_blueprint(summarize_release_bp)
app.register_blueprint(verify_receipt_bp)
app.register_blueprint(export_artifact_bp)
app.register_blueprint(verify_checkpoint_bp)
app.register_blueprint(fetch_roster_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
