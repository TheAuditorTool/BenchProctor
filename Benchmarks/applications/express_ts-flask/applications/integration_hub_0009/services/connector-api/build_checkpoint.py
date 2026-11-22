# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("build_checkpoint", __name__)


@bp.route("/build_checkpoint", methods=["POST"])
def build_checkpoint():
    heading = request.form.get('multipart_field', '')
    try:
        handshake = json.loads(heading).get('value', heading)
    except (json.JSONDecodeError, AttributeError):
        handshake = heading
    os.unlink('/var/app/data/' + str(handshake))
    return jsonify({"result": "success"})
