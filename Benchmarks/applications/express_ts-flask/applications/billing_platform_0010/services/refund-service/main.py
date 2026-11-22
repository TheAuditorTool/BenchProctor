import os
from flask import Flask

from refund_issue import bp as refund_issue_bp
from audit_bundle import bp as audit_bundle_bp
from export_summary import bp as export_summary_bp
from export_header import bp as export_header_bp
from format_statement import bp as format_statement_bp
from compact_dunning import bp as compact_dunning_bp
from compact_digest import bp as compact_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(refund_issue_bp)
app.register_blueprint(audit_bundle_bp)
app.register_blueprint(export_summary_bp)
app.register_blueprint(export_header_bp)
app.register_blueprint(format_statement_bp)
app.register_blueprint(compact_dunning_bp)
app.register_blueprint(compact_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
