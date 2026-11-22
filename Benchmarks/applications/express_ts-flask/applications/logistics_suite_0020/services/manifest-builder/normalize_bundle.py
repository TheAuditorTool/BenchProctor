# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_bundle", __name__)


@bp.route("/normalize_bundle", methods=["POST"])
def normalize_bundle():
    transcript = request.form.get('field', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    subprocess.run(['echo', consignment], shell=False)
    return jsonify({"result": "success"})
