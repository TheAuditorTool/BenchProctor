# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_carrier", __name__)


@bp.route("/enrich_carrier", methods=["POST"])
def enrich_carrier():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return jsonify({"result": "success"})
