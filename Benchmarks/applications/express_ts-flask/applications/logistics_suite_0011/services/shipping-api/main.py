import os
from flask import Flask

from shipment_quote import bp as shipment_quote_bp
from audit_roster import bp as audit_roster_bp
from format_batch import bp as format_batch_bp
from audit_ledger import bp as audit_ledger_bp
from collect_label import bp as collect_label_bp
from enrich_index import bp as enrich_index_bp
from merge_roster import bp as merge_roster_bp
from publish_report import bp as publish_report_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(shipment_quote_bp)
app.register_blueprint(audit_roster_bp)
app.register_blueprint(format_batch_bp)
app.register_blueprint(audit_ledger_bp)
app.register_blueprint(collect_label_bp)
app.register_blueprint(enrich_index_bp)
app.register_blueprint(merge_roster_bp)
app.register_blueprint(publish_report_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
