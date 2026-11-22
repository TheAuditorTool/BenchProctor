# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_summary", __name__)


@bp.route("/audit_summary", methods=["POST"])
def audit_summary():
    snippet = (request.get_json(silent=True) or {}).get('payload', '')
    addendum = snippet if snippet else 'default'
    os.system('echo ' + str(addendum))
    return jsonify({"result": "success"})
