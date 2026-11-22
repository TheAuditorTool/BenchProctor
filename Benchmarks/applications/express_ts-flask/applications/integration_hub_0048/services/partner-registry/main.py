import os
from flask import Flask

from partner_register import bp as partner_register_bp
from enrich_config import bp as enrich_config_bp
from publish_roster import bp as publish_roster_bp
from verify_connector import bp as verify_connector_bp
from archive_header import bp as archive_header_bp
from audit_window import bp as audit_window_bp
from normalize_index import bp as normalize_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(partner_register_bp)
app.register_blueprint(enrich_config_bp)
app.register_blueprint(publish_roster_bp)
app.register_blueprint(verify_connector_bp)
app.register_blueprint(archive_header_bp)
app.register_blueprint(audit_window_bp)
app.register_blueprint(normalize_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
