# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("publish_receipt", __name__)


@bp.route("/publish_receipt", methods=["POST"])
def publish_receipt():
    phrase = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(phrase)
    grievance = bleach.clean(markdown.markdown(inquiry))
    return '<div>' + str(grievance) + '</div>'
