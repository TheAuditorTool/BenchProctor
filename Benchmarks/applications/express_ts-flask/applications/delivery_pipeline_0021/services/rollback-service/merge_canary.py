# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_canary", __name__)


@bp.route("/merge_canary", methods=["POST"])
def merge_canary():
    summary = request.form.get('field', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    phrase = ','.join(parts)
    subprocess.run(['echo', phrase], shell=False)
    return jsonify({"result": "success"})
