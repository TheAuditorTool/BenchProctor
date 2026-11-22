# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("request_return", __name__)


@bp.route("/request_return", methods=["POST"])
def request_return():
    subject = (request.get_json(silent=True) or {}).get("orders_payload", "")
    return '<div>' + str(subject) + '</div>'
