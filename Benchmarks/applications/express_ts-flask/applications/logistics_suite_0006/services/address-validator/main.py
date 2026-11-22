import os
from flask import Flask

from address_validate import bp as address_validate_bp
from summarize_label import bp as summarize_label_bp
from validate_report import bp as validate_report_bp
from format_batch import bp as format_batch_bp
from audit_checkpoint import bp as audit_checkpoint_bp
from annotate_window import bp as annotate_window_bp
from publish_record import bp as publish_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(address_validate_bp)
app.register_blueprint(summarize_label_bp)
app.register_blueprint(validate_report_bp)
app.register_blueprint(format_batch_bp)
app.register_blueprint(audit_checkpoint_bp)
app.register_blueprint(annotate_window_bp)
app.register_blueprint(publish_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
