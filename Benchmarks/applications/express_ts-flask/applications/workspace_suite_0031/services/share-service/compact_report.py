# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("compact_report", __name__)


@bp.route("/compact_report", methods=["POST"])
def compact_report():
    caption = request.cookies.get('session_token', '')
    if caption:
        synopsis = caption
    else:
        synopsis = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(synopsis)):
        return jsonify({'error': 'forbidden'}), 400
    snippet = synopsis
    subprocess.run('echo ' + str(snippet), shell=True)
    return jsonify({"result": "success"})
