# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_checkpoint", __name__)


@bp.route("/summarize_checkpoint", methods=["POST"])
def summarize_checkpoint():
    note = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    if inquiry not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    grievance = inquiry
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return jsonify({"result": "success"})
