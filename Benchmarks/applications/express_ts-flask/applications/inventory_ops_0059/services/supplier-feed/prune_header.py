# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_header", __name__)


@bp.route("/prune_header", methods=["POST"])
def prune_header():
    memo = (request.get_json(silent=True) or {}).get('payload', '')
    backorder = memo if memo else 'default'
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
