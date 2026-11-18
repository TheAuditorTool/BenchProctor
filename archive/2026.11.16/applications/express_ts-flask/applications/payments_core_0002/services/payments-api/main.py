import os
from flask import Flask

from payment_authorize import bp as payment_authorize_bp
from format_window import bp as format_window_bp
from annotate_index import bp as annotate_index_bp
from load_batch import bp as load_batch_bp
from export_policy import bp as export_policy_bp
from rotate_payout import bp as rotate_payout_bp
from merge_profile import bp as merge_profile_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(payment_authorize_bp)
app.register_blueprint(format_window_bp)
app.register_blueprint(annotate_index_bp)
app.register_blueprint(load_batch_bp)
app.register_blueprint(export_policy_bp)
app.register_blueprint(rotate_payout_bp)
app.register_blueprint(merge_profile_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
