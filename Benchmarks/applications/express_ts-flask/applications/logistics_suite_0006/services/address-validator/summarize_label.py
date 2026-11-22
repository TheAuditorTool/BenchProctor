# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("summarize_label", __name__)


@bp.route("/summarize_label", methods=["POST"])
def summarize_label():
    summary = request.args.get('id', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    return '<div>' + str(consignment) + '</div>'
