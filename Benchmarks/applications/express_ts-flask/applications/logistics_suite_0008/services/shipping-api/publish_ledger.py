# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_ledger", __name__)


@bp.route("/publish_ledger", methods=["POST"])
def publish_ledger():
    caption = request.headers.get('Referer', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return jsonify({"result": "success"})
