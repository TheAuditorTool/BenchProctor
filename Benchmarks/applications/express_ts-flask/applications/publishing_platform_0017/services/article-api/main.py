import os
from flask import Flask

from article_draft import bp as article_draft_bp
from audit_checkpoint import bp as audit_checkpoint_bp
from verify_digest import bp as verify_digest_bp
from fetch_header import bp as fetch_header_bp
from render_article import bp as render_article_bp
from resolve_batch import bp as resolve_batch_bp
from audit_header import bp as audit_header_bp
from rotate_ledger import bp as rotate_ledger_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(article_draft_bp)
app.register_blueprint(audit_checkpoint_bp)
app.register_blueprint(verify_digest_bp)
app.register_blueprint(fetch_header_bp)
app.register_blueprint(render_article_bp)
app.register_blueprint(resolve_batch_bp)
app.register_blueprint(audit_header_bp)
app.register_blueprint(rotate_ledger_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
