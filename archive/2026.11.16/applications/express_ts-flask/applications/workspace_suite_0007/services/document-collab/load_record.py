# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, request


bp = Blueprint("load_record", __name__)


@bp.route("/load_record", methods=["POST"])
def load_record():
    summary = request.headers.get('Authorization', '')
    subtitle = base64.b64decode(summary).decode('utf-8', 'ignore')
    return '<div>' + str(subtitle) + '</div>'
