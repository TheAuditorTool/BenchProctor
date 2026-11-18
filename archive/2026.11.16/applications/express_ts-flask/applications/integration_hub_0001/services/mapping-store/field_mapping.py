# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("map_field", __name__)


@bp.route("/map_field", methods=["POST"])
def map_field():
    synopsis = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    return '<div>' + str(synopsis) + '</div>'
