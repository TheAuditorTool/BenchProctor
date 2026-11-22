# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("upload_document", __name__)


@bp.route("/upload_document", methods=["POST"])
def upload_document():
    transcript = (request.get_json(silent=True) or {}).get("documents_payload", "")
    subprocess.run('echo ' + str(transcript), shell=True)
    return jsonify({"result": "success"})
