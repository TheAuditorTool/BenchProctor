# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("audit_threshold", __name__)


@bp.route("/audit_threshold", methods=["POST"])
def audit_threshold():
    subject = request.headers.get('X-Custom-Header', '')
    if subject:
        ledger = subject
    else:
        ledger = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return jsonify({'error': 'forbidden'}), 400
    disbursement = ledger
    return '<div>' + str(disbursement) + '</div>'
