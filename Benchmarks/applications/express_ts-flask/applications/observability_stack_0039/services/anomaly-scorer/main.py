import os
from flask import Flask

from anomaly_score import bp as anomaly_score_bp
from render_schedule import bp as render_schedule_bp
from load_index import bp as load_index_bp
from enrich_metric import bp as enrich_metric_bp
from rotate_digest import bp as rotate_digest_bp
from verify_report import bp as verify_report_bp
from rotate_trace import bp as rotate_trace_bp
from format_report import bp as format_report_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(anomaly_score_bp)
app.register_blueprint(render_schedule_bp)
app.register_blueprint(load_index_bp)
app.register_blueprint(enrich_metric_bp)
app.register_blueprint(rotate_digest_bp)
app.register_blueprint(verify_report_bp)
app.register_blueprint(rotate_trace_bp)
app.register_blueprint(format_report_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
