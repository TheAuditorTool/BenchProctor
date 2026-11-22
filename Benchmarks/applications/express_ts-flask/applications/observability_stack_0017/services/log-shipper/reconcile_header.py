# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_header", __name__)


@bp.route("/reconcile_header", methods=["POST"])
def reconcile_header():
    note = request.form.get('multipart_field', '')
    parts = str(note).split(',')
    cohort = ' '.join(parts)
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
