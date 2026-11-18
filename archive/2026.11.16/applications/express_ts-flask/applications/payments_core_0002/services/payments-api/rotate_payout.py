# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_payout", __name__)


@bp.route("/rotate_payout", methods=["POST"])
def rotate_payout():
    subtitle = request.headers.get('Referer', '')
    ledger = (lambda v: v.strip())(subtitle)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", ledger):
        return jsonify({'error': 'forbidden'}), 400
    remittance = ledger
    subprocess.run('echo ' + str(remittance), shell=True)
    return jsonify({"result": "success"})
