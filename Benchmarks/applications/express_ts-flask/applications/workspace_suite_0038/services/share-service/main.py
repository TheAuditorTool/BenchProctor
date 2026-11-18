import os
from flask import Flask

from share_grant import bp as share_grant_bp
from annotate_digest import bp as annotate_digest_bp
from rotate_digest import bp as rotate_digest_bp
from export_digest import bp as export_digest_bp
from format_comment import bp as format_comment_bp
from prune_schedule import bp as prune_schedule_bp
from fetch_digest import bp as fetch_digest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(share_grant_bp)
app.register_blueprint(annotate_digest_bp)
app.register_blueprint(rotate_digest_bp)
app.register_blueprint(export_digest_bp)
app.register_blueprint(format_comment_bp)
app.register_blueprint(prune_schedule_bp)
app.register_blueprint(fetch_digest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
