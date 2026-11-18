# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("compact_record", __name__)


@bp.route("/compact_record", methods=["POST"])
def compact_record():
    passage = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(passage)
    disbursement = bleach.clean(markdown.markdown(remittance))
    return '<div>' + str(disbursement) + '</div>'
