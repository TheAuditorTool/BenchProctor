# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("push_syndication", __name__)


@bp.route("/push_syndication", methods=["POST"])
def push_syndication():
    excerpt = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    addendum = os.path.join('/var/app/data', os.path.basename(excerpt))
    os.unlink(addendum)
    return jsonify({"result": "success"})
