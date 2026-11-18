# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("annotate_index", __name__)


@bp.route("/annotate_index", methods=["POST"])
def annotate_index():
    subtitle = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    ledger = normalize(subtitle)
    remittance = bleach.clean(markdown.markdown(ledger))
    return '<div>' + str(remittance) + '</div>'
