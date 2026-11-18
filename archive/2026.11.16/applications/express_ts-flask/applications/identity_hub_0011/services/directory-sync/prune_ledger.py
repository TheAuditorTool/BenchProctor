# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_ledger", __name__)


@bp.route("/prune_ledger", methods=["POST"])
def prune_ledger():
    excerpt = request.files['upload'].filename
    persona = f'{excerpt!s}'
    requests.get(str(persona))
    return jsonify({"result": "success"})
