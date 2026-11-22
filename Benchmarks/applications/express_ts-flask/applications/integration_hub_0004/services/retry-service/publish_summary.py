# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_summary", __name__)


@bp.route("/publish_summary", methods=["POST"])
def publish_summary():
    summary = request.args.get('id', '')
    handshake, _sep, _rest = str(summary).partition('\x00')
    subprocess.run('echo ' + str(handshake), shell=True)
    return jsonify({"result": "success"})
