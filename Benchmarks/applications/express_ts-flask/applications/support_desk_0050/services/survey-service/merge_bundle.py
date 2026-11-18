# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_bundle", __name__)


@bp.route("/merge_bundle", methods=["POST"])
def merge_bundle():
    remark = request.headers.get('X-Custom-Header', '')
    if remark:
        inquiry = remark
    else:
        inquiry = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    return '<div>' + str(grievance) + '</div>'
