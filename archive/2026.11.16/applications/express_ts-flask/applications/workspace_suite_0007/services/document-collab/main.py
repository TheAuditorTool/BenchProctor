import os
from flask import Flask

from document_edit import bp as document_edit_bp
from load_roster import bp as load_roster_bp
from load_record import bp as load_record_bp
from render_checkpoint import bp as render_checkpoint_bp
from enrich_digest import bp as enrich_digest_bp
from build_index import bp as build_index_bp
from load_summary import bp as load_summary_bp
from summarize_digest import bp as summarize_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(document_edit_bp)
app.register_blueprint(load_roster_bp)
app.register_blueprint(load_record_bp)
app.register_blueprint(render_checkpoint_bp)
app.register_blueprint(enrich_digest_bp)
app.register_blueprint(build_index_bp)
app.register_blueprint(load_summary_bp)
app.register_blueprint(summarize_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
