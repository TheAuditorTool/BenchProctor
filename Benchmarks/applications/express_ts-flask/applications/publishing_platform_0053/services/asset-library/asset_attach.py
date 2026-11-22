# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("attach_asset", __name__)


@bp.route("/attach_asset", methods=["POST"])
def attach_asset():
    remark = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    return '<div>' + str(remark) + '</div>'
