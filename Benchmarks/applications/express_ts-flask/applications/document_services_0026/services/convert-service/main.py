import os
from flask import Flask

from convert_job import bp as convert_job_bp
from render_snapshot import bp as render_snapshot_bp
from compact_roster import bp as compact_roster_bp
from render_conversion import bp as render_conversion_bp
from collect_snapshot import bp as collect_snapshot_bp
from archive_bundle import bp as archive_bundle_bp
from build_manifest import bp as build_manifest_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(convert_job_bp)
app.register_blueprint(render_snapshot_bp)
app.register_blueprint(compact_roster_bp)
app.register_blueprint(render_conversion_bp)
app.register_blueprint(collect_snapshot_bp)
app.register_blueprint(archive_bundle_bp)
app.register_blueprint(build_manifest_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
