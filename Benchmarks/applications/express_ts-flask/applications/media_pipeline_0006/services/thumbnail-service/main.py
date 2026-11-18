import os
from flask import Flask

from thumbnail_render import bp as thumbnail_render_bp
from fetch_ledger import bp as fetch_ledger_bp
from build_roster import bp as build_roster_bp
from render_schedule import bp as render_schedule_bp
from annotate_caption import bp as annotate_caption_bp
from load_threshold import bp as load_threshold_bp
from rotate_index import bp as rotate_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(thumbnail_render_bp)
app.register_blueprint(fetch_ledger_bp)
app.register_blueprint(build_roster_bp)
app.register_blueprint(render_schedule_bp)
app.register_blueprint(annotate_caption_bp)
app.register_blueprint(load_threshold_bp)
app.register_blueprint(rotate_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
