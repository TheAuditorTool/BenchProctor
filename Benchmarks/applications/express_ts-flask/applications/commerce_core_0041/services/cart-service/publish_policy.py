# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("publish_policy", __name__)


@bp.route("/publish_policy", methods=["POST"])
def publish_policy():
    headline = request.get_data(as_text=True)
    reader = make_reader(headline)
    backorder = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    voucher = backorder
    subprocess.Popen('echo ' + str(voucher), shell=True).wait()
    return jsonify({"result": "success"})
