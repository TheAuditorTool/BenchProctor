import os
from flask import Flask

from return_request import bp as return_request_bp
from compact_record import bp as compact_record_bp
from annotate_order import bp as annotate_order_bp
from normalize_receipt import bp as normalize_receipt_bp
from reconcile_policy import bp as reconcile_policy_bp
from rotate_index import bp as rotate_index_bp
from audit_roster import bp as audit_roster_bp
from render_bundle import bp as render_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(return_request_bp)
app.register_blueprint(compact_record_bp)
app.register_blueprint(annotate_order_bp)
app.register_blueprint(normalize_receipt_bp)
app.register_blueprint(reconcile_policy_bp)
app.register_blueprint(rotate_index_bp)
app.register_blueprint(audit_roster_bp)
app.register_blueprint(render_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
