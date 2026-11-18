import os
from flask import Flask

from return_request import bp as return_request_bp
from compact_window import bp as compact_window_bp
from archive_ledger import bp as archive_ledger_bp
from export_window import bp as export_window_bp
from collect_ledger import bp as collect_ledger_bp
from rotate_window import bp as rotate_window_bp
from compact_record import bp as compact_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(return_request_bp)
app.register_blueprint(compact_window_bp)
app.register_blueprint(archive_ledger_bp)
app.register_blueprint(export_window_bp)
app.register_blueprint(collect_ledger_bp)
app.register_blueprint(rotate_window_bp)
app.register_blueprint(compact_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
