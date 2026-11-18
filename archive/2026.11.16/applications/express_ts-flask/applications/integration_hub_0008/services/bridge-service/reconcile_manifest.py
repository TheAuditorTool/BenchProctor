# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_manifest", __name__)


@bp.route("/reconcile_manifest", methods=["POST"])
def reconcile_manifest():
    preface = request.headers.get('Referer', '')
    handshake = (lambda v: v.strip())(preface)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    paragraph = handshake
    subprocess.run('echo ' + str(paragraph), shell=True)
    return jsonify({"result": "success"})
