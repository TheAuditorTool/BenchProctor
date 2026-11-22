# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_receipt", __name__)


@bp.route("/merge_receipt", methods=["POST"])
def merge_receipt():
    remark = request.form.get('multipart_field', '')
    parts = str(remark).split(',')
    gauge = ' '.join(parts)
    parsed = json.loads(gauge)
    return jsonify({'parsed': str(parsed)}), 200
