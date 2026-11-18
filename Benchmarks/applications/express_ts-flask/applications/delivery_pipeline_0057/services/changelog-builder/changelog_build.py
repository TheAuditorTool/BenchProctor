# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("build_changelog", __name__)


@bp.route("/build_changelog", methods=["POST"])
def build_changelog():
    tagline = (request.get_json(silent=True) or {}).get("delivery_payload", "")
    return '<div>' + str(tagline) + '</div>'
