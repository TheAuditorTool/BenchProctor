import os
from flask import Flask

from knowledge_search import bp as knowledge_search_bp
from summarize_receipt import bp as summarize_receipt_bp
from format_record import bp as format_record_bp
from summarize_checkpoint import bp as summarize_checkpoint_bp
from enrich_threshold import bp as enrich_threshold_bp
from load_ledger import bp as load_ledger_bp
from render_ticket import bp as render_ticket_bp
from fetch_window import bp as fetch_window_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(knowledge_search_bp)
app.register_blueprint(summarize_receipt_bp)
app.register_blueprint(format_record_bp)
app.register_blueprint(summarize_checkpoint_bp)
app.register_blueprint(enrich_threshold_bp)
app.register_blueprint(load_ledger_bp)
app.register_blueprint(render_ticket_bp)
app.register_blueprint(fetch_window_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
