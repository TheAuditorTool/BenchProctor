import os
from flask import Flask

from promo_apply import bp as promo_apply_bp
from merge_manifest import bp as merge_manifest_bp
from merge_profile import bp as merge_profile_bp
from resolve_cart import bp as resolve_cart_bp
from prune_promotion import bp as prune_promotion_bp
from collect_threshold import bp as collect_threshold_bp
from archive_policy import bp as archive_policy_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(promo_apply_bp)
app.register_blueprint(merge_manifest_bp)
app.register_blueprint(merge_profile_bp)
app.register_blueprint(resolve_cart_bp)
app.register_blueprint(prune_promotion_bp)
app.register_blueprint(collect_threshold_bp)
app.register_blueprint(archive_policy_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
