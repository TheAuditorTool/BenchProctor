import os
from flask import Flask

from ocr_extract import bp as ocr_extract_bp
from publish_checkpoint import bp as publish_checkpoint_bp
from annotate_schedule import bp as annotate_schedule_bp
from compact_header import bp as compact_header_bp
from render_conversion import bp as render_conversion_bp
from render_attachment import bp as render_attachment_bp
from normalize_config import bp as normalize_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(ocr_extract_bp)
app.register_blueprint(publish_checkpoint_bp)
app.register_blueprint(annotate_schedule_bp)
app.register_blueprint(compact_header_bp)
app.register_blueprint(render_conversion_bp)
app.register_blueprint(render_attachment_bp)
app.register_blueprint(normalize_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
