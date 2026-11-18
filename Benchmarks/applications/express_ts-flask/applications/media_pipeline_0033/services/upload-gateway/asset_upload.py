# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("upload_asset", __name__)


@bp.route("/upload_asset", methods=["POST"])
def upload_asset():
    blurb = (request.get_json(silent=True) or {}).get("media_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(blurb)):
        return jsonify({'error': 'forbidden'}), 400
    montage = blurb
    subprocess.Popen('echo ' + str(montage), shell=True).wait()
    return jsonify({"result": "success"})
