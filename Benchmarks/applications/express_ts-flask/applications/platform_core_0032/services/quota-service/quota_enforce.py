# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
from flask import request


bp = Blueprint("enforce_quota", __name__)


@bp.route("/enforce_quota", methods=["POST"])
def enforce_quota():
    passage = (request.get_json(silent=True) or {}).get("platform_payload", "")
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(passage) + '</div>')
    return resp
