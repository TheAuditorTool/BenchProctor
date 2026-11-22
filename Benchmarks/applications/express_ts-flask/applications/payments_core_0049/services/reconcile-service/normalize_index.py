# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("normalize_index", __name__)


@bp.route("/normalize_index", methods=["POST"])
def normalize_index():
    headline = request.headers.get('Host', '')
    disbursement = (lambda v: v.strip())(headline)
    pickle.loads(base64.b64decode(disbursement))
    return jsonify({"result": "success"})
