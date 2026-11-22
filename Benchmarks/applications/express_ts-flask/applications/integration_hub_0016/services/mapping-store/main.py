import os
from flask import Flask

from field_mapping import bp as field_mapping_bp
from format_mapping import bp as format_mapping_bp
from merge_manifest import bp as merge_manifest_bp
from publish_connector import bp as publish_connector_bp
from prune_index import bp as prune_index_bp
from validate_snapshot import bp as validate_snapshot_bp
from export_record import bp as export_record_bp

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.get("/health")
def health():
    return {"status": "ok"}


app.register_blueprint(field_mapping_bp)
app.register_blueprint(format_mapping_bp)
app.register_blueprint(merge_manifest_bp)
app.register_blueprint(publish_connector_bp)
app.register_blueprint(prune_index_bp)
app.register_blueprint(validate_snapshot_bp)
app.register_blueprint(export_record_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
