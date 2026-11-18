import os
from flask import Flask

from tracking_poll import bp as tracking_poll_bp
from load_profile import bp as load_profile_bp
from render_checkpoint import bp as render_checkpoint_bp
from merge_window import bp as merge_window_bp
from format_receipt import bp as format_receipt_bp
from compact_carrier import bp as compact_carrier_bp
from annotate_snapshot import bp as annotate_snapshot_bp
from collect_label import bp as collect_label_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(tracking_poll_bp)
app.register_blueprint(load_profile_bp)
app.register_blueprint(render_checkpoint_bp)
app.register_blueprint(merge_window_bp)
app.register_blueprint(format_receipt_bp)
app.register_blueprint(compact_carrier_bp)
app.register_blueprint(annotate_snapshot_bp)
app.register_blueprint(collect_label_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
