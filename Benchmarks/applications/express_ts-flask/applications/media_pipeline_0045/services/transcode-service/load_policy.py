# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("load_policy", __name__)


@bp.route("/load_policy", methods=["POST"])
def load_policy():
    notice = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(notice)
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
