# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_manifest", __name__)


@bp.route("/publish_manifest", methods=["POST"])
def publish_manifest():
    heading = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(heading)
    parsed = json.loads(consignment)
    return jsonify({'parsed': str(parsed)}), 200
