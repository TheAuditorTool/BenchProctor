# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("annotate_macro", __name__)


@bp.route("/annotate_macro", methods=["POST"])
def annotate_macro():
    citation = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    grievance = normalize(citation)
    inquiry = bleach.clean(markdown.markdown(grievance))
    return '<div>' + str(inquiry) + '</div>'
