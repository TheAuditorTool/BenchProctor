import os
from flask import Flask

from connector_invoke import bp as connector_invoke_bp
from format_digest import bp as format_digest_bp
from archive_connector import bp as archive_connector_bp
from load_batch import bp as load_batch_bp
from collect_digest import bp as collect_digest_bp
from normalize_window import bp as normalize_window_bp
from format_policy import bp as format_policy_bp
from resolve_mapping import bp as resolve_mapping_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(connector_invoke_bp)
app.register_blueprint(format_digest_bp)
app.register_blueprint(archive_connector_bp)
app.register_blueprint(load_batch_bp)
app.register_blueprint(collect_digest_bp)
app.register_blueprint(normalize_window_bp)
app.register_blueprint(format_policy_bp)
app.register_blueprint(resolve_mapping_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
