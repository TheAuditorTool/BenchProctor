# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_config", __name__)


@bp.route("/archive_config", methods=["POST"])
def archive_config():
    caption = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(caption)
    subprocess.run('echo ' + str(parcel), shell=True)
    return jsonify({"result": "success"})
