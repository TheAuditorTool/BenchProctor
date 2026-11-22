import os
from flask import Flask

from payout_schedule import bp as payout_schedule_bp
from fetch_mandate import bp as fetch_mandate_bp
from annotate_checkpoint import bp as annotate_checkpoint_bp
from build_config import bp as build_config_bp
from archive_schedule import bp as archive_schedule_bp
from verify_digest import bp as verify_digest_bp
from collect_index import bp as collect_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payout_schedule_bp)
app.register_blueprint(fetch_mandate_bp)
app.register_blueprint(annotate_checkpoint_bp)
app.register_blueprint(build_config_bp)
app.register_blueprint(archive_schedule_bp)
app.register_blueprint(verify_digest_bp)
app.register_blueprint(collect_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
