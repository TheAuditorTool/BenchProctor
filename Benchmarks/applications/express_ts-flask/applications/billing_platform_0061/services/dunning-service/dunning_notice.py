# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("send_dunning_notice", __name__)


@bp.route("/send_dunning_notice", methods=["POST"])
def send_dunning_notice():
    dunning = (request.get_json(silent=True) or {}).get("billing_payload", "")
    os.unlink('/var/app/data/' + str(dunning))
    return jsonify({"result": "success"})
