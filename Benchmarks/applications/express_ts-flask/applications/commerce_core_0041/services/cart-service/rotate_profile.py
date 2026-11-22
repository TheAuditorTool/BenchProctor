# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_profile", __name__)


@bp.route("/rotate_profile", methods=["POST"])
def rotate_profile():
    headline = request.headers.get('Referer', '')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    backorder = ','.join(parts)
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
