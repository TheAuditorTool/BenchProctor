import os
from flask import Flask

from redaction_apply import bp as redaction_apply_bp
from compact_index import bp as compact_index_bp
from compact_digest import bp as compact_digest_bp
from publish_summary import bp as publish_summary_bp
from reconcile_index import bp as reconcile_index_bp
from summarize_record import bp as summarize_record_bp
from fetch_config import bp as fetch_config_bp
from fetch_index import bp as fetch_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(redaction_apply_bp)
app.register_blueprint(compact_index_bp)
app.register_blueprint(compact_digest_bp)
app.register_blueprint(publish_summary_bp)
app.register_blueprint(reconcile_index_bp)
app.register_blueprint(summarize_record_bp)
app.register_blueprint(fetch_config_bp)
app.register_blueprint(fetch_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
