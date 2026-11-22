# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("verify_window", __name__)


@bp.route("/verify_window", methods=["POST"])
def verify_window():
    paragraph = request.cookies.get('session_token', '')
    if paragraph:
        persona = paragraph
    else:
        persona = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return jsonify({'error': 'forbidden'}), 400
    blurb = persona
    subprocess.run('echo ' + str(blurb), shell=True)
    return jsonify({"result": "success"})
