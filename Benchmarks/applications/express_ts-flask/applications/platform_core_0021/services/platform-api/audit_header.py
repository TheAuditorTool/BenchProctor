# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("audit_header", __name__)


@bp.route("/audit_header", methods=["POST"])
def audit_header():
    excerpt = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(excerpt)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return jsonify({'error': 'forbidden'}), 400
    persona = handshake
    subprocess.Popen('echo ' + str(persona), shell=True).wait()
    return jsonify({"result": "success"})
