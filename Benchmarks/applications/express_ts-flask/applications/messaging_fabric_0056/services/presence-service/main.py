import os
from flask import Flask

from presence_update import bp as presence_update_bp
from format_header import bp as format_header_bp
from collect_bundle import bp as collect_bundle_bp
from merge_ledger import bp as merge_ledger_bp
from load_message import bp as load_message_bp
from verify_header import bp as verify_header_bp
from load_record import bp as load_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(presence_update_bp)
app.register_blueprint(format_header_bp)
app.register_blueprint(collect_bundle_bp)
app.register_blueprint(merge_ledger_bp)
app.register_blueprint(load_message_bp)
app.register_blueprint(verify_header_bp)
app.register_blueprint(load_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
