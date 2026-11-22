import os
from flask import Flask

from syndication_push import bp as syndication_push_bp
from annotate_index import bp as annotate_index_bp
from prune_syndication import bp as prune_syndication_bp
from reconcile_window import bp as reconcile_window_bp
from summarize_config import bp as summarize_config_bp
from format_checkpoint import bp as format_checkpoint_bp
from fetch_summary import bp as fetch_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(syndication_push_bp)
app.register_blueprint(annotate_index_bp)
app.register_blueprint(prune_syndication_bp)
app.register_blueprint(reconcile_window_bp)
app.register_blueprint(summarize_config_bp)
app.register_blueprint(format_checkpoint_bp)
app.register_blueprint(fetch_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
