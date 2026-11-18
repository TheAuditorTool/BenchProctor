# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_summary", __name__)


@bp.route("/enrich_summary", methods=["POST"])
def enrich_summary():
    paragraph = request.get_data(as_text=True)
    bulletin = ' '.join(str(paragraph).split())
    requests.get(str(bulletin))
    return jsonify({"result": "success"})
