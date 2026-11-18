# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_trace", __name__)


@bp.route("/fetch_trace", methods=["POST"])
def fetch_trace():
    summary = request.headers.get('X-Custom-Header', '')
    if summary:
        gauge = summary
    else:
        gauge = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    return '<div>' + str(cohort) + '</div>'
