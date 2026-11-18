# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("annotate_schedule", __name__)


@bp.route("/annotate_schedule", methods=["POST"])
def annotate_schedule():
    note = request.form.get('field', '')
    addendum = f'{note!s}'
    parsed = json.loads(addendum)
    return jsonify({'parsed': str(parsed)}), 200
