# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("track_presence", __name__)


@bp.route("/track_presence", methods=["POST"])
def track_presence():
    transcript = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(transcript)):
        return jsonify({'error': 'forbidden'}), 400
    quotation = transcript
    os.unlink('/var/app/data/' + str(quotation))
    return jsonify({"result": "success"})
