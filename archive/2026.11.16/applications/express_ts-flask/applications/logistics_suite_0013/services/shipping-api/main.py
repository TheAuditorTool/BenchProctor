import os
from flask import Flask

from shipment_quote import bp as shipment_quote_bp
from compact_window import bp as compact_window_bp
from render_ledger import bp as render_ledger_bp
from validate_checkpoint import bp as validate_checkpoint_bp
from render_waybill import bp as render_waybill_bp
from merge_roster import bp as merge_roster_bp
from reconcile_summary import bp as reconcile_summary_bp
from export_ledger import bp as export_ledger_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(shipment_quote_bp)
app.register_blueprint(compact_window_bp)
app.register_blueprint(render_ledger_bp)
app.register_blueprint(validate_checkpoint_bp)
app.register_blueprint(render_waybill_bp)
app.register_blueprint(merge_roster_bp)
app.register_blueprint(reconcile_summary_bp)
app.register_blueprint(export_ledger_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
