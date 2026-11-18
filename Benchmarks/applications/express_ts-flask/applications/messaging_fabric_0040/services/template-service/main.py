import os
from flask import Flask

from template_compose import bp as template_compose_bp
from annotate_window import bp as annotate_window_bp
from normalize_profile import bp as normalize_profile_bp
from collect_summary import bp as collect_summary_bp
from prune_roster import bp as prune_roster_bp
from validate_schedule import bp as validate_schedule_bp
from verify_delivery import bp as verify_delivery_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(template_compose_bp)
app.register_blueprint(annotate_window_bp)
app.register_blueprint(normalize_profile_bp)
app.register_blueprint(collect_summary_bp)
app.register_blueprint(prune_roster_bp)
app.register_blueprint(validate_schedule_bp)
app.register_blueprint(verify_delivery_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
