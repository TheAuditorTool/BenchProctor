# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_roster", __name__)


@bp.route("/audit_roster", methods=["POST"])
def audit_roster():
    citation = (request.get_json(silent=True) or {}).get('payload', '')
    consignment = citation if citation else 'default'
    os.system('echo ' + str(consignment))
    return jsonify({"result": "success"})
