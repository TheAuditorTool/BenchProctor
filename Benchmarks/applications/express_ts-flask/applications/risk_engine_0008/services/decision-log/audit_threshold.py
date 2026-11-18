# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_threshold", __name__)


@bp.route("/audit_threshold", methods=["POST"])
def audit_threshold():
    synopsis = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(synopsis).split(','):
        parts.append(token.strip())
    verdict = ','.join(parts)
    if verdict not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    grievance = verdict
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return jsonify({"result": "success"})
