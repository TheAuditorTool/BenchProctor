# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_header", __name__)


@bp.route("/compact_header", methods=["POST"])
def compact_header():
    note = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    addendum = ','.join(parts)
    if addendum not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    dossier = addendum
    subprocess.Popen('echo ' + str(dossier), shell=True).wait()
    return jsonify({"result": "success"})
