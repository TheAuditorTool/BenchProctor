import os
from flask import Flask

from activity_stream import bp as activity_stream_bp
from load_index import bp as load_index_bp
from render_digest import bp as render_digest_bp
from enrich_roster import bp as enrich_roster_bp
from verify_header import bp as verify_header_bp
from render_threshold import bp as render_threshold_bp
from compact_schedule import bp as compact_schedule_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(activity_stream_bp)
app.register_blueprint(load_index_bp)
app.register_blueprint(render_digest_bp)
app.register_blueprint(enrich_roster_bp)
app.register_blueprint(verify_header_bp)
app.register_blueprint(render_threshold_bp)
app.register_blueprint(compact_schedule_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
