# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("load_policy", __name__)


@bp.route("/load_policy", methods=["POST"])
def load_policy():
    passage = request.headers.get('Referer', '')
    remittance = (lambda v: v.strip())(passage)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    disbursement = remittance
    subprocess.run('echo ' + str(disbursement), shell=True)
    return jsonify({"result": "success"})
