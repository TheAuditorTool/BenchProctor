import os
from flask import Flask

from rate_shop import bp as rate_shop_bp
from enrich_checkpoint import bp as enrich_checkpoint_bp
from audit_threshold import bp as audit_threshold_bp
from annotate_threshold import bp as annotate_threshold_bp
from collect_index import bp as collect_index_bp
from merge_ledger import bp as merge_ledger_bp
from rotate_manifest import bp as rotate_manifest_bp
from publish_manifest import bp as publish_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(rate_shop_bp)
app.register_blueprint(enrich_checkpoint_bp)
app.register_blueprint(audit_threshold_bp)
app.register_blueprint(annotate_threshold_bp)
app.register_blueprint(collect_index_bp)
app.register_blueprint(merge_ledger_bp)
app.register_blueprint(rotate_manifest_bp)
app.register_blueprint(publish_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
