# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("export_ledger", __name__)


@bp.route("/export_ledger", methods=["POST"])
def export_ledger():
    footnote = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(footnote)
    consignment = bleach.clean(markdown.markdown(parcel))
    return '<div>' + str(consignment) + '</div>'
