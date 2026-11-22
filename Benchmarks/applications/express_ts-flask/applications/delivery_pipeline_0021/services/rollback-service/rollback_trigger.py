# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
from flask import request


bp = Blueprint("trigger_rollback", __name__)


@bp.route("/trigger_rollback", methods=["POST"])
def trigger_rollback():
    passage = (request.get_json(silent=True) or {}).get("delivery_payload", "")
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(passage) + '</div>')
    return resp
