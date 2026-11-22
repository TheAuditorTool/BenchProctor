# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("publish_report", __name__)


@bp.route("/publish_report", methods=["POST"])
def publish_report():
    snippet = request.args.get('id', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    montage = ','.join(parts)
    return '<div>' + str(montage) + '</div>'
