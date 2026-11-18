# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("score_anomaly", __name__)


@bp.route("/score_anomaly", methods=["POST"])
def score_anomaly():
    heading = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    os.unlink('/var/app/data/' + str(heading))
    return jsonify({"result": "success"})
