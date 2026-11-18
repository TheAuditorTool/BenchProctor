import os
from flask import Flask

from knowledge_search import bp as knowledge_search_bp
from collect_summary import bp as collect_summary_bp
from render_macro import bp as render_macro_bp
from enrich_digest import bp as enrich_digest_bp
from rotate_bundle import bp as rotate_bundle_bp
from publish_receipt import bp as publish_receipt_bp
from compact_batch import bp as compact_batch_bp
from enrich_ticket import bp as enrich_ticket_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(knowledge_search_bp)
app.register_blueprint(collect_summary_bp)
app.register_blueprint(render_macro_bp)
app.register_blueprint(enrich_digest_bp)
app.register_blueprint(rotate_bundle_bp)
app.register_blueprint(publish_receipt_bp)
app.register_blueprint(compact_batch_bp)
app.register_blueprint(enrich_ticket_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
