# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("build_policy", __name__)


@bp.route("/build_policy", methods=["POST"])
def build_policy():
    summary = request.args.get('id', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    gauge = ','.join(parts)
    return '<div>' + str(gauge) + '</div>'
