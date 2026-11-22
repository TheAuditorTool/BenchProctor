# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("format_window", __name__)


@bp.route("/format_window", methods=["POST"])
def format_window():
    headline = request.get_data(as_text=True)
    reader = make_reader(headline)
    disbursement = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", disbursement):
        return jsonify({'error': 'forbidden'}), 400
    remittance = disbursement
    subprocess.Popen('echo ' + str(remittance), shell=True).wait()
    return jsonify({"result": "success"})
