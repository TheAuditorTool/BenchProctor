# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("sync_directory", __name__)


@bp.route("/sync_directory", methods=["POST"])
def sync_directory():
    synopsis = (request.get_json(silent=True) or {}).get("identity_payload", "")
    subprocess.run('echo ' + str(synopsis), shell=True)
    return jsonify({"result": "success"})
