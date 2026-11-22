# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_ledger", __name__)


@bp.route("/enrich_ledger", methods=["POST"])
def enrich_ledger():
    snippet = (request.get_json(silent=True) or {}).get('payload', '')
    montage = snippet if snippet else 'default'
    os.system('echo ' + str(montage))
    return jsonify({"result": "success"})
