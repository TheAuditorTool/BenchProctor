# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_index", __name__)


@bp.route("/merge_index", methods=["POST"])
def merge_index():
    blurb = request.form.get('field', '')
    parts = []
    for token in str(blurb).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    subprocess.run(['echo', inquiry], shell=False)
    return jsonify({"result": "success"})
