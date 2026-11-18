import os
from flask import Flask

from capture_settle import bp as capture_settle_bp
from compact_index import bp as compact_index_bp
from compact_record import bp as compact_record_bp
from verify_ledger import bp as verify_ledger_bp
from load_policy import bp as load_policy_bp
from render_window import bp as render_window_bp
from format_config import bp as format_config_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(capture_settle_bp)
app.register_blueprint(compact_index_bp)
app.register_blueprint(compact_record_bp)
app.register_blueprint(verify_ledger_bp)
app.register_blueprint(load_policy_bp)
app.register_blueprint(render_window_bp)
app.register_blueprint(format_config_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
