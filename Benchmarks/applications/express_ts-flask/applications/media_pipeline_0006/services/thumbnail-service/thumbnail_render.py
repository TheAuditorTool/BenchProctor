# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("render_thumbnail", __name__)


@bp.route("/render_thumbnail", methods=["POST"])
def render_thumbnail():
    subject = (request.get_json(silent=True) or {}).get("media_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", subject):
        return jsonify({'error': 'forbidden'}), 400
    rendition = subject
    return '<div>' + str(rendition) + '</div>'
