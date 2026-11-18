# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("annotate_profile", __name__)


@bp.route("/annotate_profile", methods=["POST"])
def annotate_profile():
    note = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(note)
    parsed = json.loads(handshake)
    return jsonify({'parsed': str(parsed)}), 200
