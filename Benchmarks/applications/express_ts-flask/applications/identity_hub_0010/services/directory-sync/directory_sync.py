# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("sync_directory", __name__)


@bp.route("/sync_directory", methods=["POST"])
def sync_directory():
    note = (request.get_json(silent=True) or {}).get("identity_payload", "")
    return '<div>' + str(note) + '</div>'
