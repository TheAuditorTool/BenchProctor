# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_receipt", __name__)


@bp.route("/collect_receipt", methods=["POST"])
def collect_receipt():
    snippet = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    if persona not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    synopsis = persona
    subprocess.Popen('echo ' + str(synopsis), shell=True).wait()
    return jsonify({"result": "success"})
