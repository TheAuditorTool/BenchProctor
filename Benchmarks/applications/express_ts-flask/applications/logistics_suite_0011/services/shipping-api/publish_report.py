# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_report", __name__)


@bp.route("/publish_report", methods=["POST"])
def publish_report():
    citation = request.form.get('field', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    subprocess.run(['echo', consignment], shell=False)
    return jsonify({"result": "success"})
