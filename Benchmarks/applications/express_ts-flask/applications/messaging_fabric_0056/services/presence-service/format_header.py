# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("format_header", __name__)


@bp.route("/format_header", methods=["POST"])
def format_header():
    footnote = request.args.get('id', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    return '<div>' + str(bulletin) + '</div>'
