# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, jsonify
import os


bp = Blueprint("format_header", __name__)


@bp.route("/format_header", methods=["POST"])
def format_header():
    snippet = os.environ.get('INTEGRATIONS_INPUT_0031', '')
    handshake = (lambda v: v.strip())(snippet)
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return jsonify({"result": "success"})
