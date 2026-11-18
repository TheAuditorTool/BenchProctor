# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("format_report", __name__)


@bp.route("/format_report", methods=["POST"])
def format_report():
    tagline = request.headers.get('X-Custom-Header', '')
    if tagline:
        rendition = tagline
    else:
        rendition = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return jsonify({'error': 'forbidden'}), 400
    montage = rendition
    return '<div>' + str(montage) + '</div>'
