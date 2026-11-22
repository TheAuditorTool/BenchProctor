import os
from flask import Flask

from audit_append import bp as audit_append_bp
from render_secret import bp as render_secret_bp
from validate_tenant import bp as validate_tenant_bp
from normalize_flag import bp as normalize_flag_bp
from archive_checkpoint import bp as archive_checkpoint_bp
from validate_policy import bp as validate_policy_bp
from fetch_roster import bp as fetch_roster_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(audit_append_bp)
app.register_blueprint(render_secret_bp)
app.register_blueprint(validate_tenant_bp)
app.register_blueprint(normalize_flag_bp)
app.register_blueprint(archive_checkpoint_bp)
app.register_blueprint(validate_policy_bp)
app.register_blueprint(fetch_roster_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
