import os
from flask import Flask

from syndication_push import bp as syndication_push_bp
from enrich_summary import bp as enrich_summary_bp
from export_config import bp as export_config_bp
from fetch_taxonomy import bp as fetch_taxonomy_bp
from compact_roster import bp as compact_roster_bp
from merge_header import bp as merge_header_bp
from compact_revision import bp as compact_revision_bp
from enrich_threshold import bp as enrich_threshold_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(syndication_push_bp)
app.register_blueprint(enrich_summary_bp)
app.register_blueprint(export_config_bp)
app.register_blueprint(fetch_taxonomy_bp)
app.register_blueprint(compact_roster_bp)
app.register_blueprint(merge_header_bp)
app.register_blueprint(compact_revision_bp)
app.register_blueprint(enrich_threshold_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
