import os
from flask import Flask

from field_mapping import bp as field_mapping_bp
from collect_bundle import bp as collect_bundle_bp
from rotate_receipt import bp as rotate_receipt_bp
from fetch_config import bp as fetch_config_bp
from resolve_summary import bp as resolve_summary_bp
from export_summary import bp as export_summary_bp
from publish_snapshot import bp as publish_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(field_mapping_bp)
app.register_blueprint(collect_bundle_bp)
app.register_blueprint(rotate_receipt_bp)
app.register_blueprint(fetch_config_bp)
app.register_blueprint(resolve_summary_bp)
app.register_blueprint(export_summary_bp)
app.register_blueprint(publish_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
