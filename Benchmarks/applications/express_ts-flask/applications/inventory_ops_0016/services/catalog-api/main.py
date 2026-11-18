import os
from flask import Flask

from sku_lookup import bp as sku_lookup_bp
from collect_schedule import bp as collect_schedule_bp
from export_digest import bp as export_digest_bp
from rotate_threshold import bp as rotate_threshold_bp
from fetch_supplier import bp as fetch_supplier_bp
from summarize_reservation import bp as summarize_reservation_bp
from format_digest import bp as format_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(sku_lookup_bp)
app.register_blueprint(collect_schedule_bp)
app.register_blueprint(export_digest_bp)
app.register_blueprint(rotate_threshold_bp)
app.register_blueprint(fetch_supplier_bp)
app.register_blueprint(summarize_reservation_bp)
app.register_blueprint(format_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
