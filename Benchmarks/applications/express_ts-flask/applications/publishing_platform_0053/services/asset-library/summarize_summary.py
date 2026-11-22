# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("summarize_summary", __name__)


@bp.route("/summarize_summary", methods=["POST"])
def summarize_summary():
    note = request.headers.get('Host', '')
    byline = (lambda v: v.strip())(note)
    pickle.loads(base64.b64decode(byline))
    return jsonify({"result": "success"})
