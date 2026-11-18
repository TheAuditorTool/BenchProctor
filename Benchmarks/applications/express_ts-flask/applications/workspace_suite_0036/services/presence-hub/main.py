import os
from flask import Flask

from presence_track import bp as presence_track_bp
from resolve_receipt import bp as resolve_receipt_bp
from rotate_document import bp as rotate_document_bp
from build_window import bp as build_window_bp
from annotate_report import bp as annotate_report_bp
from compact_window import bp as compact_window_bp
from verify_receipt import bp as verify_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(presence_track_bp)
app.register_blueprint(resolve_receipt_bp)
app.register_blueprint(rotate_document_bp)
app.register_blueprint(build_window_bp)
app.register_blueprint(annotate_report_bp)
app.register_blueprint(compact_window_bp)
app.register_blueprint(verify_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
