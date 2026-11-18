# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, jsonify
import os


bp = Blueprint("fetch_roster", __name__)


@bp.route("/fetch_roster", methods=["POST"])
def fetch_roster():
    heading = os.environ.get('ORDERS_INPUT_0007', '')
    voucher = (lambda v: v.strip())(heading)
    subprocess.Popen('echo ' + str(voucher), shell=True).wait()
    return jsonify({"result": "success"})
