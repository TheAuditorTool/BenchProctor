import os
from flask import Flask

from metric_ingest import bp as metric_ingest_bp
from summarize_trace import bp as summarize_trace_bp
from verify_index import bp as verify_index_bp
from normalize_alert import bp as normalize_alert_bp
from load_threshold import bp as load_threshold_bp
from rotate_policy import bp as rotate_policy_bp
from merge_summary import bp as merge_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(metric_ingest_bp)
app.register_blueprint(summarize_trace_bp)
app.register_blueprint(verify_index_bp)
app.register_blueprint(normalize_alert_bp)
app.register_blueprint(load_threshold_bp)
app.register_blueprint(rotate_policy_bp)
app.register_blueprint(merge_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
