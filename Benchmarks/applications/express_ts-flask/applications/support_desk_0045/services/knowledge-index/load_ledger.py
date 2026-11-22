# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("load_ledger", __name__)


@bp.route("/load_ledger", methods=["POST"])
def load_ledger():
    remark = request.form.get('multipart_field', '')
    parts = str(remark).split(',')
    inquiry = ' '.join(parts)
    parsed = json.loads(inquiry)
    return jsonify({'parsed': str(parsed)}), 200
