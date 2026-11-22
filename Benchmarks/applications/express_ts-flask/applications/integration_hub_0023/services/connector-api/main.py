import os
from flask import Flask

from connector_invoke import bp as connector_invoke_bp
from reconcile_snapshot import bp as reconcile_snapshot_bp
from verify_threshold import bp as verify_threshold_bp
from merge_receipt import bp as merge_receipt_bp
from load_partner import bp as load_partner_bp
from render_roster import bp as render_roster_bp
from verify_manifest import bp as verify_manifest_bp
from load_summary import bp as load_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(connector_invoke_bp)
app.register_blueprint(reconcile_snapshot_bp)
app.register_blueprint(verify_threshold_bp)
app.register_blueprint(merge_receipt_bp)
app.register_blueprint(load_partner_bp)
app.register_blueprint(render_roster_bp)
app.register_blueprint(verify_manifest_bp)
app.register_blueprint(load_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
