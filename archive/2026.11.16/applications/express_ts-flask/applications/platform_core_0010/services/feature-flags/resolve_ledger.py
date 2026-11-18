# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_ledger", __name__)


@bp.route("/resolve_ledger", methods=["POST"])
def resolve_ledger():
    notice = request.headers.get('Referer', '')
    persona = (lambda v: v.strip())(notice)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    subprocess.run('echo ' + str(handshake), shell=True)
    return jsonify({"result": "success"})
