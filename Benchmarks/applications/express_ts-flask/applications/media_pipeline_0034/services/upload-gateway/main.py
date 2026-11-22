import os
from flask import Flask

from asset_upload import bp as asset_upload_bp
from summarize_record import bp as summarize_record_bp
from render_caption import bp as render_caption_bp
from export_profile import bp as export_profile_bp
from validate_schedule import bp as validate_schedule_bp
from validate_checkpoint import bp as validate_checkpoint_bp
from reconcile_report import bp as reconcile_report_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(asset_upload_bp)
app.register_blueprint(summarize_record_bp)
app.register_blueprint(render_caption_bp)
app.register_blueprint(export_profile_bp)
app.register_blueprint(validate_schedule_bp)
app.register_blueprint(validate_checkpoint_bp)
app.register_blueprint(reconcile_report_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
