# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_roster", __name__)


@bp.route("/enrich_roster", methods=["POST"])
def enrich_roster():
    phrase = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(phrase)
    parsed = json.loads(parcel)
    return jsonify({'parsed': str(parsed)}), 200
