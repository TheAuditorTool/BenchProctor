# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("audit_escalation", __name__)


@bp.route("/audit_escalation", methods=["POST"])
def audit_escalation():
    summary = request.form.get('field', '')
    grievance = f'{summary!s}'
    parsed = json.loads(grievance)
    return jsonify({'parsed': str(parsed)}), 200
