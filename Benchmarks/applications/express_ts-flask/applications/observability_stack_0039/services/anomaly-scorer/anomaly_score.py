# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("score_anomaly", __name__)


@bp.route("/score_anomaly", methods=["POST"])
def score_anomaly():
    citation = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    subprocess.run('echo ' + str(citation), shell=True)
    return jsonify({"result": "success"})
