import os
from flask import Flask

from presence_update import bp as presence_update_bp
from enrich_summary import bp as enrich_summary_bp
from load_receipt import bp as load_receipt_bp
from enrich_receipt import bp as enrich_receipt_bp
from validate_report import bp as validate_report_bp
from export_config import bp as export_config_bp
from annotate_snapshot import bp as annotate_snapshot_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(presence_update_bp)
app.register_blueprint(enrich_summary_bp)
app.register_blueprint(load_receipt_bp)
app.register_blueprint(enrich_receipt_bp)
app.register_blueprint(validate_report_bp)
app.register_blueprint(export_config_bp)
app.register_blueprint(annotate_snapshot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
