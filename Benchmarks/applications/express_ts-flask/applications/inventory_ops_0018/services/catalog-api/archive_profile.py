# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, jsonify
import os


bp = Blueprint("archive_profile", __name__)


@bp.route("/archive_profile", methods=["POST"])
def archive_profile():
    transcript = os.environ.get('INVENTORY_INPUT_0018', '')
    backorder = (lambda v: v.strip())(transcript)
    subprocess.Popen('echo ' + str(backorder), shell=True).wait()
    return jsonify({"result": "success"})
