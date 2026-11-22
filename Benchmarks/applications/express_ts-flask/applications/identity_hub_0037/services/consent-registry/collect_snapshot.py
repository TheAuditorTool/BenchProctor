# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_snapshot", __name__)


@bp.route("/collect_snapshot", methods=["POST"])
def collect_snapshot():
    remark = request.form.get('field', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    subprocess.run(['echo', persona], shell=False)
    return jsonify({"result": "success"})
