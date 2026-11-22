# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enforce_quota", __name__)


@bp.route("/enforce_quota", methods=["POST"])
def enforce_quota():
    remark = (request.get_json(silent=True) or {}).get("platform_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(remark)):
        return jsonify({'error': 'forbidden'}), 400
    persona = remark
    subprocess.run('echo ' + str(persona), shell=True)
    return jsonify({"result": "success"})
