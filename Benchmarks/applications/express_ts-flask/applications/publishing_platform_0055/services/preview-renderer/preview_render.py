# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("render_preview", __name__)


@bp.route("/render_preview", methods=["POST"])
def render_preview():
    snippet = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    os.system('echo ' + str(snippet))
    return jsonify({"result": "success"})
