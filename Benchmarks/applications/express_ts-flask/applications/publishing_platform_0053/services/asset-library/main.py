import os
from flask import Flask

from asset_attach import bp as asset_attach_bp
from export_article import bp as export_article_bp
from summarize_summary import bp as summarize_summary_bp
from summarize_revision import bp as summarize_revision_bp
from enrich_schedule import bp as enrich_schedule_bp
from merge_revision import bp as merge_revision_bp
from format_index import bp as format_index_bp
from fetch_config import bp as fetch_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(asset_attach_bp)
app.register_blueprint(export_article_bp)
app.register_blueprint(summarize_summary_bp)
app.register_blueprint(summarize_revision_bp)
app.register_blueprint(enrich_schedule_bp)
app.register_blueprint(merge_revision_bp)
app.register_blueprint(format_index_bp)
app.register_blueprint(fetch_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
