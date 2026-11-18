# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("load_report", __name__)


@bp.route("/load_report", methods=["POST"])
def load_report():
    note = request.get_data(as_text=True)
    inquiry = ' '.join(str(note).split())
    requests.get(str(inquiry))
    return jsonify({"result": "success"})
