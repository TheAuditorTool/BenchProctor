# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_snapshot", __name__)


@bp.route("/archive_snapshot", methods=["POST"])
def archive_snapshot():
    citation = request.headers.get('Referer', '')
    grievance = (lambda v: v.strip())(citation)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return jsonify({"result": "success"})
