# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_partner", __name__)


@bp.route("/prune_partner", methods=["POST"])
def prune_partner():
    summary = request.get_data(as_text=True)
    handshake = (lambda v: v.strip())(summary)
    parsed = json.loads(handshake)
    return jsonify({'parsed': str(parsed)}), 200
