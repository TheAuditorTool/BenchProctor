# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("render_batch", __name__)


@bp.route("/render_batch", methods=["POST"])
def render_batch():
    remark = request.headers.get('User-Agent', '')
    requests.get(str(remark))
    return jsonify({"result": "success"})
