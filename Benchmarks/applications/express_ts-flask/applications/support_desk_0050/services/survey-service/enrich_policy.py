# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("enrich_policy", __name__)


@bp.route("/enrich_policy", methods=["POST"])
def enrich_policy():
    remark = request.args.get('id', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    return '<div>' + str(inquiry) + '</div>'
