# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_snapshot", __name__)


@bp.route("/resolve_snapshot", methods=["POST"])
def resolve_snapshot():
    note = request.get_data(as_text=True)
    reader = make_reader(note)
    cohort = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", cohort):
        return jsonify({'error': 'forbidden'}), 400
    gauge = cohort
    subprocess.Popen('echo ' + str(gauge), shell=True).wait()
    return jsonify({"result": "success"})
