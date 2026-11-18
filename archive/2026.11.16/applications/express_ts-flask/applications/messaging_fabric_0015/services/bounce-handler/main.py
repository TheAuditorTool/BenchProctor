import os
from flask import Flask

from bounce_record import bp as bounce_record_bp
from build_receipt import bp as build_receipt_bp
from export_snapshot import bp as export_snapshot_bp
from collect_message import bp as collect_message_bp
from render_delivery import bp as render_delivery_bp
from render_config import bp as render_config_bp
from prune_message import bp as prune_message_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(bounce_record_bp)
app.register_blueprint(build_receipt_bp)
app.register_blueprint(export_snapshot_bp)
app.register_blueprint(collect_message_bp)
app.register_blueprint(render_delivery_bp)
app.register_blueprint(render_config_bp)
app.register_blueprint(prune_message_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
