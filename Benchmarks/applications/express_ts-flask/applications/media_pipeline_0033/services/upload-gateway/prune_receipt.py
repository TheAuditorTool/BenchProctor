# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_receipt", __name__)


@bp.route("/prune_receipt", methods=["POST"])
def prune_receipt():
    transcript = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(transcript)
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
