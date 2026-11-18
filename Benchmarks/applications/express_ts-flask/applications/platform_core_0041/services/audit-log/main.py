import os
from flask import Flask

from audit_append import bp as audit_append_bp
from load_header import bp as load_header_bp
from compact_flag import bp as compact_flag_bp
from export_flag import bp as export_flag_bp
from resolve_index import bp as resolve_index_bp
from annotate_secret import bp as annotate_secret_bp
from fetch_summary import bp as fetch_summary_bp
from build_index import bp as build_index_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(audit_append_bp)
app.register_blueprint(load_header_bp)
app.register_blueprint(compact_flag_bp)
app.register_blueprint(export_flag_bp)
app.register_blueprint(resolve_index_bp)
app.register_blueprint(annotate_secret_bp)
app.register_blueprint(fetch_summary_bp)
app.register_blueprint(build_index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
