# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("verify_receipt", __name__)


@bp.route("/verify_receipt", methods=["POST"])
def verify_receipt():
    excerpt = request.args.get('id', '')
    handshake, _sep, _rest = str(excerpt).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    persona = handshake
    subprocess.run('echo ' + str(persona), shell=True)
    return jsonify({"result": "success"})
