import os
from flask import Flask

from presence_update import bp as presence_update_bp
from annotate_report import bp as annotate_report_bp
from export_bundle import bp as export_bundle_bp
from fetch_bundle import bp as fetch_bundle_bp
from audit_batch import bp as audit_batch_bp
from enrich_record import bp as enrich_record_bp
from normalize_record import bp as normalize_record_bp
from enrich_delivery import bp as enrich_delivery_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(presence_update_bp)
app.register_blueprint(annotate_report_bp)
app.register_blueprint(export_bundle_bp)
app.register_blueprint(fetch_bundle_bp)
app.register_blueprint(audit_batch_bp)
app.register_blueprint(enrich_record_bp)
app.register_blueprint(normalize_record_bp)
app.register_blueprint(enrich_delivery_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
