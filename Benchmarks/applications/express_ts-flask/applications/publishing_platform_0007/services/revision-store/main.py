import os
from flask import Flask

from revision_save import bp as revision_save_bp
from build_index import bp as build_index_bp
from load_roster import bp as load_roster_bp
from render_snapshot import bp as render_snapshot_bp
from compact_ledger import bp as compact_ledger_bp
from annotate_record import bp as annotate_record_bp
from format_revision import bp as format_revision_bp
from summarize_roster import bp as summarize_roster_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(revision_save_bp)
app.register_blueprint(build_index_bp)
app.register_blueprint(load_roster_bp)
app.register_blueprint(render_snapshot_bp)
app.register_blueprint(compact_ledger_bp)
app.register_blueprint(annotate_record_bp)
app.register_blueprint(format_revision_bp)
app.register_blueprint(summarize_roster_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
