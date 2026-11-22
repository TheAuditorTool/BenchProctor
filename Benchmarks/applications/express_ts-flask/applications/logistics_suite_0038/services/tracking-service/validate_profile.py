# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("validate_profile", __name__)


@bp.route("/validate_profile", methods=["POST"])
def validate_profile():
    wording = request.args.get('id', '')
    parts = []
    for token in str(wording).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    return '<div>' + str(consignment) + '</div>'
