# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_comment", __name__)


@bp.route("/format_comment", methods=["POST"])
def format_comment():
    preface = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    remark = normalize(preface)
    parsed = json.loads(remark)
    return jsonify({'parsed': str(parsed)}), 200
