import os
from flask import Flask

from payment_authorize import bp as payment_authorize_bp
from publish_dispute import bp as publish_dispute_bp
from archive_digest import bp as archive_digest_bp
from annotate_header import bp as annotate_header_bp
from publish_summary import bp as publish_summary_bp
from build_digest import bp as build_digest_bp
from format_window import bp as format_window_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_authorize_bp)
app.register_blueprint(publish_dispute_bp)
app.register_blueprint(archive_digest_bp)
app.register_blueprint(annotate_header_bp)
app.register_blueprint(publish_summary_bp)
app.register_blueprint(build_digest_bp)
app.register_blueprint(format_window_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
