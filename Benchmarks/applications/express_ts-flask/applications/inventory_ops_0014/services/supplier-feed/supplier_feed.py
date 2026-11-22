# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("pull_supplier_feed", __name__)


@bp.route("/pull_supplier_feed", methods=["POST"])
def pull_supplier_feed():
    memo = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    with open('/var/app/data/' + str(memo), 'r') as fh:
        content = fh.read()
    return content
