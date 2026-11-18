import os
from flask import Flask

from field_mapping import bp as field_mapping_bp
from fetch_record import bp as fetch_record_bp
from fetch_ledger import bp as fetch_ledger_bp
from format_roster import bp as format_roster_bp
from collect_connector import bp as collect_connector_bp
from publish_summary import bp as publish_summary_bp
from archive_mapping import bp as archive_mapping_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(field_mapping_bp)
app.register_blueprint(fetch_record_bp)
app.register_blueprint(fetch_ledger_bp)
app.register_blueprint(format_roster_bp)
app.register_blueprint(collect_connector_bp)
app.register_blueprint(publish_summary_bp)
app.register_blueprint(archive_mapping_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
