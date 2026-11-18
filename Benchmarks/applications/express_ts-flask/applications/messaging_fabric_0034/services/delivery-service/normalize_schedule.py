# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_schedule", __name__)


@bp.route("/normalize_schedule", methods=["POST"])
def normalize_schedule():
    footnote = request.headers.get('User-Agent', '')
    requests.get(str(footnote))
    return jsonify({"result": "success"})
