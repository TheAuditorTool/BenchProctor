# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_cart", __name__)


@bp.route("/resolve_cart", methods=["POST"])
def resolve_cart():
    subject = request.get_data(as_text=True)
    reader = make_reader(subject)
    voucher = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", voucher):
        return jsonify({'error': 'forbidden'}), 400
    backorder = voucher
    subprocess.Popen('echo ' + str(backorder), shell=True).wait()
    return jsonify({"result": "success"})
