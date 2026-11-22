# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_profile", __name__)


@bp.route("/enrich_profile", methods=["POST"])
def enrich_profile():
    excerpt = request.get_data(as_text=True)
    restock = (lambda v: v.strip())(excerpt)
    parsed = json.loads(restock)
    return jsonify({'parsed': str(parsed)}), 200
