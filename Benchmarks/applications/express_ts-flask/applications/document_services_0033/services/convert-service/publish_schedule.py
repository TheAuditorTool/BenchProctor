# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_schedule", __name__)


@bp.route("/publish_schedule", methods=["POST"])
def publish_schedule():
    snippet = request.form.get('multipart_field', '')
    parts = str(snippet).split(',')
    addendum = ' '.join(parts)
    parsed = json.loads(addendum)
    return jsonify({'parsed': str(parsed)}), 200
