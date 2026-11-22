# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_schedule", __name__)


@bp.route("/enrich_schedule", methods=["POST"])
def enrich_schedule():
    note = request.form.get('field', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    subprocess.run(['echo', byline], shell=False)
    return jsonify({"result": "success"})
