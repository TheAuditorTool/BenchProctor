# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_promotion", __name__)


@bp.route("/publish_promotion", methods=["POST"])
def publish_promotion():
    notice = (request.get_json(silent=True) or {}).get('payload', '')
    backorder = notice if notice else 'default'
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
