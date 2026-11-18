# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("export_summary", __name__)


@bp.route("/export_summary", methods=["POST"])
def export_summary():
    summary = request.args.get('id', '')
    cohort, _sep, _rest = str(summary).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", cohort):
        return jsonify({'error': 'forbidden'}), 400
    gauge = cohort
    subprocess.run('echo ' + str(gauge), shell=True)
    return jsonify({"result": "success"})
