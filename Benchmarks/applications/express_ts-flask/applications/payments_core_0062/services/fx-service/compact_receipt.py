# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_receipt", __name__)


@bp.route("/compact_receipt", methods=["POST"])
def compact_receipt():
    headline = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    disbursement = normalize(headline)
    subprocess.Popen('echo ' + str(disbursement), shell=True).wait()
    return jsonify({"result": "success"})
