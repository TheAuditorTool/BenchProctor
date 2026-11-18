import os
from flask import Flask

from queue_bridge import bp as queue_bridge_bp
from rotate_batch import bp as rotate_batch_bp
from validate_roster import bp as validate_roster_bp
from reconcile_manifest import bp as reconcile_manifest_bp
from render_manifest import bp as render_manifest_bp
from resolve_schedule import bp as resolve_schedule_bp
from export_schedule import bp as export_schedule_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(queue_bridge_bp)
app.register_blueprint(rotate_batch_bp)
app.register_blueprint(validate_roster_bp)
app.register_blueprint(reconcile_manifest_bp)
app.register_blueprint(render_manifest_bp)
app.register_blueprint(resolve_schedule_bp)
app.register_blueprint(export_schedule_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
