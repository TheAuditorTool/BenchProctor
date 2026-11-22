import os
from flask import Flask

from ticket_route import bp as ticket_route_bp
from collect_receipt import bp as collect_receipt_bp
from summarize_config import bp as summarize_config_bp
from render_header import bp as render_header_bp
from prune_bundle import bp as prune_bundle_bp
from archive_escalation import bp as archive_escalation_bp
from prune_batch import bp as prune_batch_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(ticket_route_bp)
app.register_blueprint(collect_receipt_bp)
app.register_blueprint(summarize_config_bp)
app.register_blueprint(render_header_bp)
app.register_blueprint(prune_bundle_bp)
app.register_blueprint(archive_escalation_bp)
app.register_blueprint(prune_batch_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
