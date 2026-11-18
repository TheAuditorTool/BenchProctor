# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_batch", __name__)


@bp.route("/fetch_batch", methods=["POST"])
def fetch_batch():
    note = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(note)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return jsonify({'error': 'forbidden'}), 400
    persona = handshake
    subprocess.Popen('echo ' + str(persona), shell=True).wait()
    return jsonify({"result": "success"})
