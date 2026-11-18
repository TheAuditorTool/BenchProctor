# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_report", __name__)


@bp.route("/validate_report", methods=["POST"])
def validate_report():
    paragraph = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    if bulletin not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    synopsis = bulletin
    subprocess.Popen('echo ' + str(synopsis), shell=True).wait()
    return jsonify({"result": "success"})
