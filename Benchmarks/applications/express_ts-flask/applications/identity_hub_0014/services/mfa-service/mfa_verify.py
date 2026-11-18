# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("verify_mfa", __name__)


@bp.route("/verify_mfa", methods=["POST"])
def verify_mfa():
    notice = (request.get_json(silent=True) or {}).get("identity_payload", "")
    return '<div>' + str(notice) + '</div>'
