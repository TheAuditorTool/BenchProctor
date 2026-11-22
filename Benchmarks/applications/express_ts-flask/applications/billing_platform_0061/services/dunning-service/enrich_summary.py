# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("enrich_summary", __name__)


@bp.route("/enrich_summary", methods=["POST"])
def enrich_summary():
    footnote = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(footnote).split(',')
    remittance = ' '.join(parts)
    return '<div>' + str(remittance) + '</div>'
