# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("search_knowledge", __name__)


@bp.route("/search_knowledge", methods=["POST"])
def search_knowledge():
    excerpt = (request.get_json(silent=True) or {}).get("support_payload", "")
    subprocess.Popen('echo ' + str(excerpt), shell=True).wait()
    return jsonify({"result": "success"})
