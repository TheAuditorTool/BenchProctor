# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_summary", __name__)


@bp.route("/rotate_summary", methods=["POST"])
def rotate_summary():
    footnote = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    if byline not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    addendum = byline
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return jsonify({"result": "success"})
