# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("annotate_window", __name__)


@bp.route("/annotate_window", methods=["POST"])
def annotate_window():
    remark = request.get_data(as_text=True)
    reader = make_reader(remark)
    note = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", note):
        return jsonify({'error': 'forbidden'}), 400
    phrase = note
    subprocess.Popen('echo ' + str(phrase), shell=True).wait()
    return jsonify({"result": "success"})
