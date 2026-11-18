# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("verify_report", __name__)


@bp.route("/verify_report", methods=["POST"])
def verify_report():
    caption = request.form.get('field', '')
    cohort = f'{caption!s}'
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
