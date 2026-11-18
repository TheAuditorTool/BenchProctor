# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("apply_redaction", __name__)


@bp.route("/apply_redaction", methods=["POST"])
def apply_redaction():
    transcript = (request.get_json(silent=True) or {}).get("documents_payload", "")
    return '<div>' + str(transcript) + '</div>'
