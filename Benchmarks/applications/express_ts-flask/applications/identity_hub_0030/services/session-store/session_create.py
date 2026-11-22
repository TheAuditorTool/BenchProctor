# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("create_session", __name__)


@bp.route("/create_session", methods=["POST"])
def create_session():
    caption = (request.get_json(silent=True) or {}).get("identity_payload", "")
    subprocess.Popen('echo ' + str(caption), shell=True).wait()
    return jsonify({"result": "success"})
