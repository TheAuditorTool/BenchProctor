# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_report", __name__)


@bp.route("/collect_report", methods=["POST"])
def collect_report():
    citation = request.form.get('field', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    subprocess.run(['echo', parcel], shell=False)
    return jsonify({"result": "success"})
