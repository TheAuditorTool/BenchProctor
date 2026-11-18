# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("record_decision", __name__)


@bp.route("/record_decision", methods=["POST"])
def record_decision():
    excerpt = (request.get_json(silent=True) or {}).get("risk_payload", "")
    subprocess.Popen('echo ' + str(excerpt), shell=True).wait()
    return jsonify({"result": "success"})
