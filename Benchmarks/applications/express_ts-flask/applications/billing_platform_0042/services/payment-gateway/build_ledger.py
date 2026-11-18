# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("build_ledger", __name__)


@bp.route("/build_ledger", methods=["POST"])
def build_ledger():
    remark = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    if remittance not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    dunning = remittance
    subprocess.Popen('echo ' + str(dunning), shell=True).wait()
    return jsonify({"result": "success"})
