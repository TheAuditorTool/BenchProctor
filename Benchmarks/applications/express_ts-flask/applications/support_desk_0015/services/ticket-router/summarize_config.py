# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("summarize_config", __name__)


@bp.route("/summarize_config", methods=["POST"])
def summarize_config():
    phrase = request.get_data(as_text=True)
    reader = make_reader(phrase)
    grievance = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = grievance
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return jsonify({"result": "success"})
