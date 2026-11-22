# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
from flask import request


bp = Blueprint("pull_supplier_feed", __name__)


@bp.route("/pull_supplier_feed", methods=["POST"])
def pull_supplier_feed():
    preface = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(preface) + '</div>')
    return resp
