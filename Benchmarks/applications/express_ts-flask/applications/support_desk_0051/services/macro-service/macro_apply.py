# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("apply_macro", __name__)


@bp.route("/apply_macro", methods=["POST"])
def apply_macro():
    subtitle = (request.get_json(silent=True) or {}).get("support_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(subtitle)):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = subtitle
    os.system('echo ' + str(inquiry))
    return jsonify({"result": "success"})
