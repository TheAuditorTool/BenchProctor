# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_ledger", __name__)


@bp.route("/audit_ledger", methods=["POST"])
def audit_ledger():
    summary = request.get_data(as_text=True)
    reader = make_reader(summary)
    handshake = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    paragraph = handshake
    subprocess.Popen('echo ' + str(paragraph), shell=True).wait()
    return jsonify({"result": "success"})
