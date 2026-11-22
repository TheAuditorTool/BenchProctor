# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_receipt", __name__)


@bp.route("/reconcile_receipt", methods=["POST"])
def reconcile_receipt():
    blurb = request.get_data(as_text=True)
    reader = make_reader(blurb)
    inquiry = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return jsonify({"result": "success"})
