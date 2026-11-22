# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("render_threshold", __name__)


@bp.route("/render_threshold", methods=["POST"])
def render_threshold():
    snippet = request.form.get('field', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    addendum = ','.join(parts)
    subprocess.run(['echo', addendum], shell=False)
    return jsonify({"result": "success"})
