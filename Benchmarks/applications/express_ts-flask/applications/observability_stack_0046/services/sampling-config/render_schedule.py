# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("render_schedule", __name__)


@bp.route("/render_schedule", methods=["POST"])
def render_schedule():
    paragraph = request.form.get('field', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    gauge = ','.join(parts)
    subprocess.run(['echo', gauge], shell=False)
    return jsonify({"result": "success"})
