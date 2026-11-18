# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("summarize_header", __name__)


@bp.route("/summarize_header", methods=["POST"])
def summarize_header():
    phrase = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(phrase)
    restock = bleach.clean(markdown.markdown(backorder))
    return '<div>' + str(restock) + '</div>'
