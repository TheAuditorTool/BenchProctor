# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("search_knowledge", __name__)


@bp.route("/search_knowledge", methods=["POST"])
def search_knowledge():
    notice = (request.get_json(silent=True) or {}).get("support_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", notice):
        return jsonify({'error': 'forbidden'}), 400
    grievance = notice
    subprocess.run('echo ' + str(grievance), shell=True)
    return jsonify({"result": "success"})
