# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("reconcile_schedule", __name__)


@bp.route("/reconcile_schedule", methods=["POST"])
def reconcile_schedule():
    footnote = request.form.get('field', '')
    wording = f'{footnote!s}'
    parsed = json.loads(wording)
    return jsonify({'parsed': str(parsed)}), 200
