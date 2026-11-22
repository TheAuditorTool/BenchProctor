# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("configure_sample", __name__)


@bp.route("/configure_sample", methods=["POST"])
def configure_sample():
    blurb = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    subprocess.run(['echo', blurb], shell=False)
    return jsonify({"result": "success"})
