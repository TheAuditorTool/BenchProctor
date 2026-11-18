import os
from flask import Flask

from payment_authorize import bp as payment_authorize_bp
from publish_payout import bp as publish_payout_bp
from audit_snapshot import bp as audit_snapshot_bp
from merge_batch import bp as merge_batch_bp
from merge_receipt import bp as merge_receipt_bp
from rotate_threshold import bp as rotate_threshold_bp
from load_record import bp as load_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_authorize_bp)
app.register_blueprint(publish_payout_bp)
app.register_blueprint(audit_snapshot_bp)
app.register_blueprint(merge_batch_bp)
app.register_blueprint(merge_receipt_bp)
app.register_blueprint(rotate_threshold_bp)
app.register_blueprint(load_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
