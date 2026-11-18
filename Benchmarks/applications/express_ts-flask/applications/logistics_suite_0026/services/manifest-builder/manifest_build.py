# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("build_manifest", __name__)


@bp.route("/build_manifest", methods=["POST"])
def build_manifest():
    preface = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(preface) + "'")
    return jsonify({"result": "success"})
