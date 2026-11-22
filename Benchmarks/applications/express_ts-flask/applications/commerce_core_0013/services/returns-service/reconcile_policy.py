# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_policy", __name__)


@bp.route("/reconcile_policy", methods=["POST"])
def reconcile_policy():
    wording = request.form.get('multipart_field', '')
    parts = str(wording).split(',')
    backorder = ' '.join(parts)
    parsed = json.loads(backorder)
    return jsonify({'parsed': str(parsed)}), 200
