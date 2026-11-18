# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("merge_roster", __name__)


@bp.route("/merge_roster", methods=["POST"])
def merge_roster():
    footnote = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(footnote)
    consignment = bleach.clean(markdown.markdown(parcel))
    return '<div>' + str(consignment) + '</div>'
