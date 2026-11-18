import os
from flask import Flask

from asset_upload import bp as asset_upload_bp
from audit_config import bp as audit_config_bp
from render_receipt import bp as render_receipt_bp
from collect_bundle import bp as collect_bundle_bp
from prune_receipt import bp as prune_receipt_bp
from enrich_stream import bp as enrich_stream_bp
from export_window import bp as export_window_bp
from merge_summary import bp as merge_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(asset_upload_bp)
app.register_blueprint(audit_config_bp)
app.register_blueprint(render_receipt_bp)
app.register_blueprint(collect_bundle_bp)
app.register_blueprint(prune_receipt_bp)
app.register_blueprint(enrich_stream_bp)
app.register_blueprint(export_window_bp)
app.register_blueprint(merge_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
