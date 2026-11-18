# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("map_field", __name__)


@bp.route("/map_field", methods=["POST"])
def map_field():
    headline = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    subprocess.Popen('echo ' + str(headline), shell=True).wait()
    return jsonify({"result": "success"})
