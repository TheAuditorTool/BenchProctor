# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_schedule", __name__)


@bp.route("/compact_schedule", methods=["POST"])
def compact_schedule():
    paragraph = request.form.get('field', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    wording = ','.join(parts)
    subprocess.run(['echo', wording], shell=False)
    return jsonify({"result": "success"})
