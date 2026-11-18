# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_checkpoint", __name__)


@bp.route("/audit_checkpoint", methods=["POST"])
def audit_checkpoint():
    footnote = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    byline = normalize(footnote)
    subprocess.Popen('echo ' + str(byline), shell=True).wait()
    return jsonify({"result": "success"})
