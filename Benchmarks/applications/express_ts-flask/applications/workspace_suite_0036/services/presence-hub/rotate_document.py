# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_document", __name__)


@bp.route("/rotate_document", methods=["POST"])
def rotate_document():
    remark = request.headers.get('Authorization', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    parsed = yaml.safe_load(synopsis)
    return jsonify({'parsed': str(parsed)}), 200
