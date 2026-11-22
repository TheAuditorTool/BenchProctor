# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("compact_receipt", __name__)


@bp.route("/compact_receipt", methods=["POST"])
def compact_receipt():
    transcript = request.get_data(as_text=True)
    reader = make_reader(transcript)
    consignment = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", consignment):
        return jsonify({'error': 'forbidden'}), 400
    parcel = consignment
    subprocess.Popen('echo ' + str(parcel), shell=True).wait()
    return jsonify({"result": "success"})
