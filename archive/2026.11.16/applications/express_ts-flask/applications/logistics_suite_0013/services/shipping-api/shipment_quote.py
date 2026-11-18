# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("quote_shipment", __name__)


@bp.route("/quote_shipment", methods=["POST"])
def quote_shipment():
    caption = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    with open('/var/app/data/' + str(caption), 'r') as fh:
        content = fh.read()
    return content
