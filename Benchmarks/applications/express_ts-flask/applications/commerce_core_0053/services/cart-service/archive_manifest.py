# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_manifest", __name__)


@bp.route("/archive_manifest", methods=["POST"])
def archive_manifest():
    memo = request.headers.get('Authorization', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    parsed = yaml.safe_load(voucher)
    return jsonify({'parsed': str(parsed)}), 200
