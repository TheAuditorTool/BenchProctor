import os
from flask import Flask

from order_lookup import bp as order_lookup_bp
from publish_promotion import bp as publish_promotion_bp
from resolve_window import bp as resolve_window_bp
from render_summary import bp as render_summary_bp
from load_bundle import bp as load_bundle_bp
from merge_profile import bp as merge_profile_bp
from build_window import bp as build_window_bp
from prune_bundle import bp as prune_bundle_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(order_lookup_bp)
app.register_blueprint(publish_promotion_bp)
app.register_blueprint(resolve_window_bp)
app.register_blueprint(render_summary_bp)
app.register_blueprint(load_bundle_bp)
app.register_blueprint(merge_profile_bp)
app.register_blueprint(build_window_bp)
app.register_blueprint(prune_bundle_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
