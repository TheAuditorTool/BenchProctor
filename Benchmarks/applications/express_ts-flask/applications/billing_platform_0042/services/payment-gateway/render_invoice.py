# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("render_invoice", __name__)


@bp.route("/render_invoice", methods=["POST"])
def render_invoice():
    remark = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    parsed = json.loads(remittance)
    return jsonify({'parsed': str(parsed)}), 200
