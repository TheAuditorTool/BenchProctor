import os
from flask import Flask

from dunning_notice import bp as dunning_notice_bp
from enrich_summary import bp as enrich_summary_bp
from build_invoice import bp as build_invoice_bp
from merge_statement import bp as merge_statement_bp
from render_receipt import bp as render_receipt_bp
from rotate_record import bp as rotate_record_bp
from collect_ledger import bp as collect_ledger_bp
from validate_dunning import bp as validate_dunning_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(dunning_notice_bp)
app.register_blueprint(enrich_summary_bp)
app.register_blueprint(build_invoice_bp)
app.register_blueprint(merge_statement_bp)
app.register_blueprint(render_receipt_bp)
app.register_blueprint(rotate_record_bp)
app.register_blueprint(collect_ledger_bp)
app.register_blueprint(validate_dunning_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
