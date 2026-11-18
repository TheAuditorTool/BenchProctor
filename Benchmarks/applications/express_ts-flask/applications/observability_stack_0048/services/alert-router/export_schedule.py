# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("export_schedule", __name__)


@bp.route("/export_schedule", methods=["POST"])
def export_schedule():
    excerpt = request.args.get('id', '')
    gauge, _sep, _rest = str(excerpt).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", gauge):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    subprocess.run('echo ' + str(cohort), shell=True)
    return jsonify({"result": "success"})
