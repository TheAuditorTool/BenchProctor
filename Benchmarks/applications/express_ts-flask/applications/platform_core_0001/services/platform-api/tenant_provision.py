# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("provision_tenant", __name__)


@bp.route("/provision_tenant", methods=["POST"])
def provision_tenant():
    wording = (request.get_json(silent=True) or {}).get("platform_payload", "")
    return '<div>' + str(wording) + '</div>'
