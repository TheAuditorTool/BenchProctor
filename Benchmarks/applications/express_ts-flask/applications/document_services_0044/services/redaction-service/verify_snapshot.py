# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("verify_snapshot", __name__)


@bp.route("/verify_snapshot", methods=["POST"])
def verify_snapshot():
    phrase = request.get_data(as_text=True)
    dossier = (lambda v: v.strip())(phrase)
    parsed = json.loads(dossier)
    return jsonify({'parsed': str(parsed)}), 200
