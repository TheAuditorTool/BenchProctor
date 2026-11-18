# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_roster", __name__)


@bp.route("/compact_roster", methods=["POST"])
def compact_roster():
    summary = request.args.get('id', '')
    grievance, _sep, _rest = str(summary).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    verdict = grievance
    subprocess.run('echo ' + str(verdict), shell=True)
    return jsonify({"result": "success"})
