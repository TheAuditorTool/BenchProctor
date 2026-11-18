# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("prune_manifest", __name__)


@bp.route("/prune_manifest", methods=["POST"])
def prune_manifest():
    remark = request.get_data(as_text=True)
    inquiry = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    db.execute('SELECT * FROM users WHERE id = ?', (inquiry,))
    return jsonify({"result": "success"})
