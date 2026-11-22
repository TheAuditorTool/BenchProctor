import os
from flask import Flask

from retention_sweep import bp as retention_sweep_bp
from summarize_manifest import bp as summarize_manifest_bp
from enrich_receipt import bp as enrich_receipt_bp
from merge_receipt import bp as merge_receipt_bp
from render_manifest import bp as render_manifest_bp
from compact_batch import bp as compact_batch_bp
from load_batch import bp as load_batch_bp
from normalize_trace import bp as normalize_trace_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(retention_sweep_bp)
app.register_blueprint(summarize_manifest_bp)
app.register_blueprint(enrich_receipt_bp)
app.register_blueprint(merge_receipt_bp)
app.register_blueprint(render_manifest_bp)
app.register_blueprint(compact_batch_bp)
app.register_blueprint(load_batch_bp)
app.register_blueprint(normalize_trace_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
