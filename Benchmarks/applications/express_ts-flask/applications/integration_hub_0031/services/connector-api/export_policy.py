# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("export_policy", __name__)


@bp.route("/export_policy", methods=["POST"])
def export_policy():
    snippet = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    if handshake not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    paragraph = handshake
    subprocess.Popen('echo ' + str(paragraph), shell=True).wait()
    return jsonify({"result": "success"})
