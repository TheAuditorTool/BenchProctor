# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_header", __name__)


@bp.route("/fetch_header", methods=["POST"])
def fetch_header():
    remark = request.args.get('id', '')
    inquiry, _sep, _rest = str(remark).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    subprocess.run('echo ' + str(grievance), shell=True)
    return jsonify({"result": "success"})
