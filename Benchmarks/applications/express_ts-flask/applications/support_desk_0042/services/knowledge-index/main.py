import os
from flask import Flask

from knowledge_search import bp as knowledge_search_bp
from reconcile_batch import bp as reconcile_batch_bp
from normalize_report import bp as normalize_report_bp
from merge_index import bp as merge_index_bp
from merge_ledger import bp as merge_ledger_bp
from reconcile_receipt import bp as reconcile_receipt_bp
from export_config import bp as export_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(knowledge_search_bp)
app.register_blueprint(reconcile_batch_bp)
app.register_blueprint(normalize_report_bp)
app.register_blueprint(merge_index_bp)
app.register_blueprint(merge_ledger_bp)
app.register_blueprint(reconcile_receipt_bp)
app.register_blueprint(export_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
