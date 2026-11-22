# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_policy", __name__)


@bp.route("/normalize_policy", methods=["POST"])
def normalize_policy():
    note = (request.get_json(silent=True) or {}).get('payload', '')
    cohort = note if note else 'default'
    os.system('echo ' + str(cohort))
    return jsonify({"result": "success"})
