import os
from flask import Flask

from shipment_quote import bp as shipment_quote_bp
from render_threshold import bp as render_threshold_bp
from export_index import bp as export_index_bp
from fetch_batch import bp as fetch_batch_bp
from merge_snapshot import bp as merge_snapshot_bp
from reconcile_roster import bp as reconcile_roster_bp
from normalize_batch import bp as normalize_batch_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(shipment_quote_bp)
app.register_blueprint(render_threshold_bp)
app.register_blueprint(export_index_bp)
app.register_blueprint(fetch_batch_bp)
app.register_blueprint(merge_snapshot_bp)
app.register_blueprint(reconcile_roster_bp)
app.register_blueprint(normalize_batch_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
