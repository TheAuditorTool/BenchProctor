# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("audit_batch", __name__)


@bp.route("/audit_batch", methods=["POST"])
def audit_batch():
    heading = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(heading).split(',')
    addendum = ' '.join(parts)
    return '<div>' + str(addendum) + '</div>'
