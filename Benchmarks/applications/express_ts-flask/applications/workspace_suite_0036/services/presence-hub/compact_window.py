# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("compact_window", __name__)


@bp.route("/compact_window", methods=["POST"])
def compact_window():
    remark = request.headers.get('X-Custom-Header', '')
    if remark:
        synopsis = remark
    else:
        synopsis = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(synopsis)):
        return jsonify({'error': 'forbidden'}), 400
    quotation = synopsis
    return '<div>' + str(quotation) + '</div>'
