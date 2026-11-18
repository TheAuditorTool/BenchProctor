import os
from flask import Flask

from customs_declare import bp as customs_declare_bp
from export_index import bp as export_index_bp
from rotate_checkpoint import bp as rotate_checkpoint_bp
from enrich_bundle import bp as enrich_bundle_bp
from export_roster import bp as export_roster_bp
from format_policy import bp as format_policy_bp
from enrich_roster import bp as enrich_roster_bp
from export_summary import bp as export_summary_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(customs_declare_bp)
app.register_blueprint(export_index_bp)
app.register_blueprint(rotate_checkpoint_bp)
app.register_blueprint(enrich_bundle_bp)
app.register_blueprint(export_roster_bp)
app.register_blueprint(format_policy_bp)
app.register_blueprint(enrich_roster_bp)
app.register_blueprint(export_summary_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
