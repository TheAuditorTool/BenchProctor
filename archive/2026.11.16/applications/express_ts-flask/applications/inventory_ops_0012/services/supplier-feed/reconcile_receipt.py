# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_receipt", __name__)


@bp.route("/reconcile_receipt", methods=["POST"])
def reconcile_receipt():
    phrase = request.files['upload'].filename
    backorder = f'{phrase!s}'
    requests.get(str(backorder))
    return jsonify({"result": "success"})
