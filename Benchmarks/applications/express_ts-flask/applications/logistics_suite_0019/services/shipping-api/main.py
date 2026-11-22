import os
from flask import Flask

from shipment_quote import bp as shipment_quote_bp
from render_roster import bp as render_roster_bp
from fetch_window import bp as fetch_window_bp
from compact_config import bp as compact_config_bp
from collect_report import bp as collect_report_bp
from collect_ledger import bp as collect_ledger_bp
from normalize_digest import bp as normalize_digest_bp
from build_checkpoint import bp as build_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(shipment_quote_bp)
app.register_blueprint(render_roster_bp)
app.register_blueprint(fetch_window_bp)
app.register_blueprint(compact_config_bp)
app.register_blueprint(collect_report_bp)
app.register_blueprint(collect_ledger_bp)
app.register_blueprint(normalize_digest_bp)
app.register_blueprint(build_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
