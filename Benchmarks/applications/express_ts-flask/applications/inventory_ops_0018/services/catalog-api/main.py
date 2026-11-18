import os
from flask import Flask

from sku_lookup import bp as sku_lookup_bp
from archive_profile import bp as archive_profile_bp
from enrich_index import bp as enrich_index_bp
from compact_index import bp as compact_index_bp
from validate_batch import bp as validate_batch_bp
from validate_roster import bp as validate_roster_bp
from reconcile_record import bp as reconcile_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(sku_lookup_bp)
app.register_blueprint(archive_profile_bp)
app.register_blueprint(enrich_index_bp)
app.register_blueprint(compact_index_bp)
app.register_blueprint(validate_batch_bp)
app.register_blueprint(validate_roster_bp)
app.register_blueprint(reconcile_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
