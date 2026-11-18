# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("raise_escalation", __name__)


@bp.route("/raise_escalation", methods=["POST"])
def raise_escalation():
    notice = (request.get_json(silent=True) or {}).get("support_payload", "")
    if not re.fullmatch("^(asc|desc|name|created)$", str(notice)):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = notice
    return '<div>' + str(inquiry) + '</div>'
