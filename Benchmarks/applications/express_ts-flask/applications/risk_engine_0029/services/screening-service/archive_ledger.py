# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_ledger", __name__)


@bp.route("/archive_ledger", methods=["POST"])
def archive_ledger():
    subject = request.args.get('id', '')
    grievance, _sep, _rest = str(subject).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    verdict = grievance
    subprocess.run('echo ' + str(verdict), shell=True)
    return jsonify({"result": "success"})
