# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_manifest", __name__)


@bp.route("/publish_manifest", methods=["POST"])
def publish_manifest():
    citation = request.get_data(as_text=True)
    dossier = (lambda v: v.strip())(citation)
    parsed = json.loads(dossier)
    return jsonify({'parsed': str(parsed)}), 200
