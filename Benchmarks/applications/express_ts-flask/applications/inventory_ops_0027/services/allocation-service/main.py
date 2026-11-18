import os
from flask import Flask

from allocation_solve import bp as allocation_solve_bp
from audit_supplier import bp as audit_supplier_bp
from summarize_allocation import bp as summarize_allocation_bp
from validate_schedule import bp as validate_schedule_bp
from reconcile_config import bp as reconcile_config_bp
from reconcile_digest import bp as reconcile_digest_bp
from merge_threshold import bp as merge_threshold_bp
from prune_allocation import bp as prune_allocation_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(allocation_solve_bp)
app.register_blueprint(audit_supplier_bp)
app.register_blueprint(summarize_allocation_bp)
app.register_blueprint(validate_schedule_bp)
app.register_blueprint(reconcile_config_bp)
app.register_blueprint(reconcile_digest_bp)
app.register_blueprint(merge_threshold_bp)
app.register_blueprint(prune_allocation_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
