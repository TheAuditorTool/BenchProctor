import os
from flask import Flask

from preview_render import bp as preview_render_bp
from annotate_summary import bp as annotate_summary_bp
from audit_checkpoint import bp as audit_checkpoint_bp
from prune_roster import bp as prune_roster_bp
from rotate_summary import bp as rotate_summary_bp
from render_config import bp as render_config_bp
from merge_snapshot import bp as merge_snapshot_bp
from merge_digest import bp as merge_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(preview_render_bp)
app.register_blueprint(annotate_summary_bp)
app.register_blueprint(audit_checkpoint_bp)
app.register_blueprint(prune_roster_bp)
app.register_blueprint(rotate_summary_bp)
app.register_blueprint(render_config_bp)
app.register_blueprint(merge_snapshot_bp)
app.register_blueprint(merge_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
