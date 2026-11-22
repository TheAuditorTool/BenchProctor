import os
from flask import Flask

from metadata_index import bp as metadata_index_bp
from fetch_profile import bp as fetch_profile_bp
from rotate_receipt import bp as rotate_receipt_bp
from verify_record import bp as verify_record_bp
from enrich_roster import bp as enrich_roster_bp
from load_threshold import bp as load_threshold_bp
from resolve_receipt import bp as resolve_receipt_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(metadata_index_bp)
app.register_blueprint(fetch_profile_bp)
app.register_blueprint(rotate_receipt_bp)
app.register_blueprint(verify_record_bp)
app.register_blueprint(enrich_roster_bp)
app.register_blueprint(load_threshold_bp)
app.register_blueprint(resolve_receipt_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
