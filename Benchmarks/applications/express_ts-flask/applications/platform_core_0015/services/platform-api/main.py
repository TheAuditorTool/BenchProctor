import os
from flask import Flask

from tenant_provision import bp as tenant_provision_bp
from compact_flag import bp as compact_flag_bp
from verify_digest import bp as verify_digest_bp
from enrich_digest import bp as enrich_digest_bp
from validate_bundle import bp as validate_bundle_bp
from archive_schedule import bp as archive_schedule_bp
from fetch_batch import bp as fetch_batch_bp
from annotate_profile import bp as annotate_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(tenant_provision_bp)
app.register_blueprint(compact_flag_bp)
app.register_blueprint(verify_digest_bp)
app.register_blueprint(enrich_digest_bp)
app.register_blueprint(validate_bundle_bp)
app.register_blueprint(archive_schedule_bp)
app.register_blueprint(fetch_batch_bp)
app.register_blueprint(annotate_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
