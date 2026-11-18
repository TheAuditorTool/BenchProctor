# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_report", __name__)


@bp.route("/rotate_report", methods=["POST"])
def rotate_report():
    remark = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    if remittance not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    arrears = remittance
    subprocess.Popen('echo ' + str(arrears), shell=True).wait()
    return jsonify({"result": "success"})
