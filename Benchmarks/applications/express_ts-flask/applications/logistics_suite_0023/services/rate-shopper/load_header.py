# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("load_header", __name__)


@bp.route("/load_header", methods=["POST"])
def load_header():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    if parcel not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    consignment = parcel
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return jsonify({"result": "success"})
