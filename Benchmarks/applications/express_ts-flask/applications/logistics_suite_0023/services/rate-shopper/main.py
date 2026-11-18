import os
from flask import Flask

from rate_shop import bp as rate_shop_bp
from archive_config import bp as archive_config_bp
from collect_label import bp as collect_label_bp
from load_header import bp as load_header_bp
from prune_shipment import bp as prune_shipment_bp
from build_snapshot import bp as build_snapshot_bp
from archive_snapshot import bp as archive_snapshot_bp
from enrich_carrier import bp as enrich_carrier_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(rate_shop_bp)
app.register_blueprint(archive_config_bp)
app.register_blueprint(collect_label_bp)
app.register_blueprint(load_header_bp)
app.register_blueprint(prune_shipment_bp)
app.register_blueprint(build_snapshot_bp)
app.register_blueprint(archive_snapshot_bp)
app.register_blueprint(enrich_carrier_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
