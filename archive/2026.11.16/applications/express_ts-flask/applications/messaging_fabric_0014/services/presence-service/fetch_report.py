# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("fetch_report", __name__)


@bp.route("/fetch_report", methods=["POST"])
def fetch_report():
    summary = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(summary)
    notice = bleach.clean(markdown.markdown(bulletin))
    return '<div>' + str(notice) + '</div>'
