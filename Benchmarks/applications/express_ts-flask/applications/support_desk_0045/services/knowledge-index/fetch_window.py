# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_window", __name__)


@bp.route("/fetch_window", methods=["POST"])
def fetch_window():
    remark = request.form.get('field', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    subprocess.run(['echo', inquiry], shell=False)
    return jsonify({"result": "success"})
