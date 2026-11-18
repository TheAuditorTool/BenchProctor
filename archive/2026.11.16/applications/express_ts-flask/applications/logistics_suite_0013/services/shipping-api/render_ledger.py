# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, request


bp = Blueprint("render_ledger", __name__)


@bp.route("/render_ledger", methods=["POST"])
def render_ledger():
    footnote = request.headers.get('Authorization', '')
    parcel = base64.b64decode(footnote).decode('utf-8', 'ignore')
    return '<div>' + str(parcel) + '</div>'
