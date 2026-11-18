# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("load_threshold", __name__)


@bp.route("/load_threshold", methods=["POST"])
def load_threshold():
    summary = request.get_data(as_text=True)
    grievance = ' '.join(str(summary).split())
    requests.get(str(grievance))
    return jsonify({"result": "success"})
