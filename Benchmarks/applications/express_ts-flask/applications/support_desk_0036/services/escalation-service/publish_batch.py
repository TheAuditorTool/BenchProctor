# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("publish_batch", __name__)


@bp.route("/publish_batch", methods=["POST"])
def publish_batch():
    preface = request.get_data(as_text=True)
    reader = make_reader(preface)
    grievance = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = grievance
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return jsonify({"result": "success"})
