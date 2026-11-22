import os
from flask import Flask

from convert_job import bp as convert_job_bp
from build_roster import bp as build_roster_bp
from publish_header import bp as publish_header_bp
from compact_config import bp as compact_config_bp
from format_schedule import bp as format_schedule_bp
from compact_signature import bp as compact_signature_bp
from collect_batch import bp as collect_batch_bp
from summarize_threshold import bp as summarize_threshold_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(convert_job_bp)
app.register_blueprint(build_roster_bp)
app.register_blueprint(publish_header_bp)
app.register_blueprint(compact_config_bp)
app.register_blueprint(format_schedule_bp)
app.register_blueprint(compact_signature_bp)
app.register_blueprint(collect_batch_bp)
app.register_blueprint(summarize_threshold_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
