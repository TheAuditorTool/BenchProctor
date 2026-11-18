# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("annotate_threshold", __name__)


@bp.route("/annotate_threshold", methods=["POST"])
def annotate_threshold():
    heading = request.headers.get('X-Custom-Header', '')
    if heading:
        consignment = heading
    else:
        consignment = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return jsonify({'error': 'forbidden'}), 400
    parcel = consignment
    return '<div>' + str(parcel) + '</div>'
