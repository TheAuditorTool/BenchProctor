# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("rotate_checkpoint", __name__)


@bp.route("/rotate_checkpoint", methods=["POST"])
def rotate_checkpoint():
    excerpt = request.headers.get('X-Custom-Header', '')
    if excerpt:
        gauge = excerpt
    else:
        gauge = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    return '<div>' + str(cohort) + '</div>'
