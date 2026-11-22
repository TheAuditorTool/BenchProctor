import os
from flask import Flask

from manifest_build import bp as manifest_build_bp
from merge_header import bp as merge_header_bp
from verify_threshold import bp as verify_threshold_bp
from normalize_bundle import bp as normalize_bundle_bp
from prune_manifest import bp as prune_manifest_bp
from compact_receipt import bp as compact_receipt_bp
from build_checkpoint import bp as build_checkpoint_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(manifest_build_bp)
app.register_blueprint(merge_header_bp)
app.register_blueprint(verify_threshold_bp)
app.register_blueprint(normalize_bundle_bp)
app.register_blueprint(prune_manifest_bp)
app.register_blueprint(compact_receipt_bp)
app.register_blueprint(build_checkpoint_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
