# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_receipt", __name__)


@bp.route("/normalize_receipt", methods=["POST"])
def normalize_receipt():
    footnote = request.headers.get('Authorization', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    parsed = yaml.safe_load(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
