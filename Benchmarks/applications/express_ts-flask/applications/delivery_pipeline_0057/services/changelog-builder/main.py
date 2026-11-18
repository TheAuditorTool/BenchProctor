import os
from flask import Flask

from changelog_build import bp as changelog_build_bp
from prune_index import bp as prune_index_bp
from collect_digest import bp as collect_digest_bp
from reconcile_schedule import bp as reconcile_schedule_bp
from summarize_receipt import bp as summarize_receipt_bp
from export_checkpoint import bp as export_checkpoint_bp
from resolve_release import bp as resolve_release_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(changelog_build_bp)
app.register_blueprint(prune_index_bp)
app.register_blueprint(collect_digest_bp)
app.register_blueprint(reconcile_schedule_bp)
app.register_blueprint(summarize_receipt_bp)
app.register_blueprint(export_checkpoint_bp)
app.register_blueprint(resolve_release_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
