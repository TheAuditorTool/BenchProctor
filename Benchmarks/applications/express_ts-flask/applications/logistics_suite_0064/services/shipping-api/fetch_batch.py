# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_batch", __name__)


@bp.route("/fetch_batch", methods=["POST"])
def fetch_batch():
    transcript = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(transcript)
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return jsonify({"result": "success"})
