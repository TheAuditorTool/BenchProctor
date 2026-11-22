import os
from flask import Flask

from preview_render import bp as preview_render_bp
from audit_batch import bp as audit_batch_bp
from validate_snapshot import bp as validate_snapshot_bp
from compact_revision import bp as compact_revision_bp
from publish_header import bp as publish_header_bp
from summarize_syndication import bp as summarize_syndication_bp
from publish_schedule import bp as publish_schedule_bp
from normalize_bundle import bp as normalize_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(preview_render_bp)
app.register_blueprint(audit_batch_bp)
app.register_blueprint(validate_snapshot_bp)
app.register_blueprint(compact_revision_bp)
app.register_blueprint(publish_header_bp)
app.register_blueprint(summarize_syndication_bp)
app.register_blueprint(publish_schedule_bp)
app.register_blueprint(normalize_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
