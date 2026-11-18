# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_roster", __name__)


@bp.route("/merge_roster", methods=["POST"])
def merge_roster():
    synopsis = request.args.get('id', '')
    verdict, _sep, _rest = str(synopsis).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", verdict):
        return jsonify({'error': 'forbidden'}), 400
    grievance = verdict
    subprocess.run('echo ' + str(grievance), shell=True)
    return jsonify({"result": "success"})
