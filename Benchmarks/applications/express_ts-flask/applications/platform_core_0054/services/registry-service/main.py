import os
from flask import Flask

from service_register import bp as service_register_bp
from resolve_index import bp as resolve_index_bp
from normalize_roster import bp as normalize_roster_bp
from archive_batch import bp as archive_batch_bp
from collect_receipt import bp as collect_receipt_bp
from compact_bundle import bp as compact_bundle_bp
from collect_manifest import bp as collect_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(service_register_bp)
app.register_blueprint(resolve_index_bp)
app.register_blueprint(normalize_roster_bp)
app.register_blueprint(archive_batch_bp)
app.register_blueprint(collect_receipt_bp)
app.register_blueprint(compact_bundle_bp)
app.register_blueprint(collect_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
