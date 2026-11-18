# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("export_artifact", __name__)


@bp.route("/export_artifact", methods=["POST"])
def export_artifact():
    wording = request.form.get('field', '')
    remark = f'{wording!s}'
    parsed = json.loads(remark)
    return jsonify({'parsed': str(parsed)}), 200
