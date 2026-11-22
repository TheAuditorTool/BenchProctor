# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_policy", __name__)


@bp.route("/summarize_policy", methods=["POST"])
def summarize_policy():
    heading = request.headers.get('Referer', '')
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return jsonify({"result": "success"})
