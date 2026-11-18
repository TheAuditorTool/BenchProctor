# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, request


bp = Blueprint("render_checkpoint", __name__)


@bp.route("/render_checkpoint", methods=["POST"])
def render_checkpoint():
    subject = request.headers.get('Authorization', '')
    parcel = base64.b64decode(subject).decode('utf-8', 'ignore')
    return '<div>' + str(parcel) + '</div>'
