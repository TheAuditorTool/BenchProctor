import os
from flask import Flask

from search_index import bp as search_index_bp
from summarize_receipt import bp as summarize_receipt_bp
from publish_manifest import bp as publish_manifest_bp
from summarize_ledger import bp as summarize_ledger_bp
from archive_config import bp as archive_config_bp
from audit_window import bp as audit_window_bp
from normalize_profile import bp as normalize_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(search_index_bp)
app.register_blueprint(summarize_receipt_bp)
app.register_blueprint(publish_manifest_bp)
app.register_blueprint(summarize_ledger_bp)
app.register_blueprint(archive_config_bp)
app.register_blueprint(audit_window_bp)
app.register_blueprint(normalize_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
