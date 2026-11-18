# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_mapping", __name__)


@bp.route("/resolve_mapping", methods=["POST"])
def resolve_mapping():
    footnote = request.args.get('id', '')
    handshake, _sep, _rest = str(footnote).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    blurb = handshake
    subprocess.run('echo ' + str(blurb), shell=True)
    return jsonify({"result": "success"})
