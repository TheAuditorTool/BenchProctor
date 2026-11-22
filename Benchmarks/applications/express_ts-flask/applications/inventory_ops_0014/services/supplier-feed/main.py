import os
from flask import Flask

from supplier_feed import bp as supplier_feed_bp
from load_record import bp as load_record_bp
from reconcile_index import bp as reconcile_index_bp
from rotate_profile import bp as rotate_profile_bp
from enrich_profile import bp as enrich_profile_bp
from validate_receipt import bp as validate_receipt_bp
from resolve_bundle import bp as resolve_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(supplier_feed_bp)
app.register_blueprint(load_record_bp)
app.register_blueprint(reconcile_index_bp)
app.register_blueprint(rotate_profile_bp)
app.register_blueprint(enrich_profile_bp)
app.register_blueprint(validate_receipt_bp)
app.register_blueprint(resolve_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
