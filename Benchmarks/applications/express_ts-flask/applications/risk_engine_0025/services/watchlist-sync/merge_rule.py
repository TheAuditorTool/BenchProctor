# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_rule", __name__)


@bp.route("/merge_rule", methods=["POST"])
def merge_rule():
    excerpt = (request.get_json(silent=True) or {}).get('payload', '')
    verdict = excerpt if excerpt else 'default'
    os.system('echo ' + str(verdict))
    return jsonify({"result": "success"})
