# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("settle_capture", __name__)


@bp.route("/settle_capture", methods=["POST"])
def settle_capture():
    ledger = (request.get_json(silent=True) or {}).get("payments_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", ledger):
        return jsonify({'error': 'forbidden'}), 400
    disbursement = ledger
    subprocess.Popen('echo ' + str(disbursement), shell=True).wait()
    return jsonify({"result": "success"})
