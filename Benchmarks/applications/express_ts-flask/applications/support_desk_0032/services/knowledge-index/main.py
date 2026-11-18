import os
from flask import Flask

from knowledge_search import bp as knowledge_search_bp
from load_report import bp as load_report_bp
from rotate_roster import bp as rotate_roster_bp
from summarize_checkpoint import bp as summarize_checkpoint_bp
from rotate_snapshot import bp as rotate_snapshot_bp
from collect_summary import bp as collect_summary_bp
from enrich_digest import bp as enrich_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(knowledge_search_bp)
app.register_blueprint(load_report_bp)
app.register_blueprint(rotate_roster_bp)
app.register_blueprint(summarize_checkpoint_bp)
app.register_blueprint(rotate_snapshot_bp)
app.register_blueprint(collect_summary_bp)
app.register_blueprint(enrich_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
