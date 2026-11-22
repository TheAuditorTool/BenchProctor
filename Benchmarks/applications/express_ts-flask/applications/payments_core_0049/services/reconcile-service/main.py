import os
from flask import Flask

from reconcile_batch import bp as reconcile_batch_bp
from export_payout import bp as export_payout_bp
from normalize_index import bp as normalize_index_bp
from enrich_header import bp as enrich_header_bp
from enrich_config import bp as enrich_config_bp
from reconcile_digest import bp as reconcile_digest_bp
from resolve_config import bp as resolve_config_bp
from annotate_index import bp as annotate_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(reconcile_batch_bp)
app.register_blueprint(export_payout_bp)
app.register_blueprint(normalize_index_bp)
app.register_blueprint(enrich_header_bp)
app.register_blueprint(enrich_config_bp)
app.register_blueprint(reconcile_digest_bp)
app.register_blueprint(resolve_config_bp)
app.register_blueprint(annotate_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
