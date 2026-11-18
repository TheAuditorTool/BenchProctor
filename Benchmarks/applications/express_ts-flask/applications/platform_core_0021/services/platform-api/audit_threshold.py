# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_threshold", __name__)


@bp.route("/audit_threshold", methods=["POST"])
def audit_threshold():
    excerpt = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(excerpt)
    subprocess.run('echo ' + str(handshake), shell=True)
    return jsonify({"result": "success"})
