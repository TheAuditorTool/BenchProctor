# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_snapshot", __name__)


@bp.route("/validate_snapshot", methods=["POST"])
def validate_snapshot():
    summary = request.args.get('id', '')
    bulletin, _sep, _rest = str(summary).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    snippet = bulletin
    subprocess.run('echo ' + str(snippet), shell=True)
    return jsonify({"result": "success"})
