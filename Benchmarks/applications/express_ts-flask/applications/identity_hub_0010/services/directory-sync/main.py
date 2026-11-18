import os
from flask import Flask

from directory_sync import bp as directory_sync_bp
from verify_checkpoint import bp as verify_checkpoint_bp
from normalize_session import bp as normalize_session_bp
from audit_schedule import bp as audit_schedule_bp
from validate_record import bp as validate_record_bp
from reconcile_batch import bp as reconcile_batch_bp
from verify_schedule import bp as verify_schedule_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(directory_sync_bp)
app.register_blueprint(verify_checkpoint_bp)
app.register_blueprint(normalize_session_bp)
app.register_blueprint(audit_schedule_bp)
app.register_blueprint(validate_record_bp)
app.register_blueprint(reconcile_batch_bp)
app.register_blueprint(verify_schedule_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
