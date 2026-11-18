# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("format_config", __name__)


@bp.route("/format_config", methods=["POST"])
def format_config():
    passage = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(passage)
    disbursement = bleach.clean(markdown.markdown(remittance))
    return '<div>' + str(disbursement) + '</div>'
