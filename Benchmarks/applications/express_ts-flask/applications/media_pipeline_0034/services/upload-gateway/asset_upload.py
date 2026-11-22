# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("upload_asset", __name__)


@bp.route("/upload_asset", methods=["POST"])
def upload_asset():
    notice = (request.get_json(silent=True) or {}).get("media_payload", "")
    Path('/var/app/data/' + str(notice)).write_text('data')
    return jsonify({"result": "success"})
