# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_sample", __name__)


@bp.route("/reconcile_sample", methods=["POST"])
def reconcile_sample():
    excerpt = request.args.get('id', '')
    gauge, _sep, _rest = str(excerpt).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", gauge):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    subprocess.run('echo ' + str(cohort), shell=True)
    return jsonify({"result": "success"})
