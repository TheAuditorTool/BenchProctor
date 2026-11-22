# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("annotate_index", __name__)


@bp.route("/annotate_index", methods=["POST"])
def annotate_index():
    transcript = request.headers.get('Host', '')
    addendum = (lambda v: v.strip())(transcript)
    pickle.loads(base64.b64decode(addendum))
    return jsonify({"result": "success"})
