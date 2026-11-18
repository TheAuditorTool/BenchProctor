# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("verify_profile", __name__)


@bp.route("/verify_profile", methods=["POST"])
def verify_profile():
    footnote = request.args.get('id', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    return '<div>' + str(consignment) + '</div>'
