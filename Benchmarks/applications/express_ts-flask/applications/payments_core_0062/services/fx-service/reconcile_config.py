# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_config", __name__)


@bp.route("/reconcile_config", methods=["POST"])
def reconcile_config():
    headline = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    disbursement = normalize(headline)
    parsed = json.loads(disbursement)
    return jsonify({'parsed': str(parsed)}), 200
