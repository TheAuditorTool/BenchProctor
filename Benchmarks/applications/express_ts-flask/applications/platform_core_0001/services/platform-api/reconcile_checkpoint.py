# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_checkpoint", __name__)


@bp.route("/reconcile_checkpoint", methods=["POST"])
def reconcile_checkpoint():
    tagline = request.headers.get('User-Agent', '')
    requests.get(str(tagline))
    return jsonify({"result": "success"})
