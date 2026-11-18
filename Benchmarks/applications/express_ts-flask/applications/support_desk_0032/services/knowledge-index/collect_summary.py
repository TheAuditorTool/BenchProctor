# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("collect_summary", __name__)


@bp.route("/collect_summary", methods=["POST"])
def collect_summary():
    note = request.headers.get('X-Custom-Header', '')
    if note:
        inquiry = note
    else:
        inquiry = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    return '<div>' + str(grievance) + '</div>'
