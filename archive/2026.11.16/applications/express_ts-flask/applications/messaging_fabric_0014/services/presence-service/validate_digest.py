# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_digest", __name__)


@bp.route("/validate_digest", methods=["POST"])
def validate_digest():
    summary = request.headers.get('Referer', '')
    bulletin = (lambda v: v.strip())(summary)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    notice = bulletin
    subprocess.run('echo ' + str(notice), shell=True)
    return jsonify({"result": "success"})
