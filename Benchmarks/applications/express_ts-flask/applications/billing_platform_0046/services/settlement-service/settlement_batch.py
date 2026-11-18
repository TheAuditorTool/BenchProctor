# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("run_settlement", __name__)


@bp.route("/run_settlement", methods=["POST"])
def run_settlement():
    dunning = (request.get_json(silent=True) or {}).get("billing_payload", "")
    if dunning not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    arrears = dunning
    subprocess.Popen('echo ' + str(arrears), shell=True).wait()
    return jsonify({"result": "success"})
