import os
from flask import Flask

from retry_queue import bp as retry_queue_bp
from publish_summary import bp as publish_summary_bp
from audit_ledger import bp as audit_ledger_bp
from merge_config import bp as merge_config_bp
from prune_partner import bp as prune_partner_bp
from validate_connector import bp as validate_connector_bp
from normalize_checkpoint import bp as normalize_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retry_queue_bp)
app.register_blueprint(publish_summary_bp)
app.register_blueprint(audit_ledger_bp)
app.register_blueprint(merge_config_bp)
app.register_blueprint(prune_partner_bp)
app.register_blueprint(validate_connector_bp)
app.register_blueprint(normalize_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
