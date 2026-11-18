# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("export_digest", __name__)


@bp.route("/export_digest", methods=["POST"])
def export_digest():
    preface = request.form.get('field', '')
    remark = f'{preface!s}'
    parsed = json.loads(remark)
    return jsonify({'parsed': str(parsed)}), 200
