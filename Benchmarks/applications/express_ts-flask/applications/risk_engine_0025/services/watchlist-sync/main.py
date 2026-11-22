import os
from flask import Flask

from watchlist_sync import bp as watchlist_sync_bp
from reconcile_decision import bp as reconcile_decision_bp
from merge_rule import bp as merge_rule_bp
from reconcile_checkpoint import bp as reconcile_checkpoint_bp
from build_ledger import bp as build_ledger_bp
from collect_header import bp as collect_header_bp
from export_rule import bp as export_rule_bp
from fetch_bundle import bp as fetch_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(watchlist_sync_bp)
app.register_blueprint(reconcile_decision_bp)
app.register_blueprint(merge_rule_bp)
app.register_blueprint(reconcile_checkpoint_bp)
app.register_blueprint(build_ledger_bp)
app.register_blueprint(collect_header_bp)
app.register_blueprint(export_rule_bp)
app.register_blueprint(fetch_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
