# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("validate_manifest", __name__)


@bp.route("/validate_manifest", methods=["POST"])
def validate_manifest():
    preface = request.args.get('id', '')
    parts = []
    for token in str(preface).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    return '<div>' + str(grievance) + '</div>'
