import os
from flask import Flask

from delivery_dispatch import bp as delivery_dispatch_bp
from normalize_schedule import bp as normalize_schedule_bp
from resolve_checkpoint import bp as resolve_checkpoint_bp
from publish_summary import bp as publish_summary_bp
from archive_checkpoint import bp as archive_checkpoint_bp
from normalize_receipt import bp as normalize_receipt_bp
from normalize_config import bp as normalize_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(delivery_dispatch_bp)
app.register_blueprint(normalize_schedule_bp)
app.register_blueprint(resolve_checkpoint_bp)
app.register_blueprint(publish_summary_bp)
app.register_blueprint(archive_checkpoint_bp)
app.register_blueprint(normalize_receipt_bp)
app.register_blueprint(normalize_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
