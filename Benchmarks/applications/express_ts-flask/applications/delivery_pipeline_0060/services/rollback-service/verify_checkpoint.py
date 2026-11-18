# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("verify_checkpoint", __name__)


@bp.route("/verify_checkpoint", methods=["POST"])
def verify_checkpoint():
    wording = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(wording).split(','):
        parts.append(token.strip())
    remark = ','.join(parts)
    if remark not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    phrase = remark
    subprocess.Popen('echo ' + str(phrase), shell=True).wait()
    return jsonify({"result": "success"})
