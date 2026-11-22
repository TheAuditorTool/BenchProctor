# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_receipt", __name__)


@bp.route("/merge_receipt", methods=["POST"])
def merge_receipt():
    caption = request.cookies.get('session_token', '')
    if caption:
        handshake = caption
    else:
        handshake = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return jsonify({'error': 'forbidden'}), 400
    subject = handshake
    subprocess.run('echo ' + str(subject), shell=True)
    return jsonify({"result": "success"})
