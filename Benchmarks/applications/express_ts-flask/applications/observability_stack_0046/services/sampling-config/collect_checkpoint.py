# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_checkpoint", __name__)


@bp.route("/collect_checkpoint", methods=["POST"])
def collect_checkpoint():
    paragraph = request.get_data(as_text=True)
    gauge = (lambda v: v.strip())(paragraph)
    parsed = json.loads(gauge)
    return jsonify({'parsed': str(parsed)}), 200
