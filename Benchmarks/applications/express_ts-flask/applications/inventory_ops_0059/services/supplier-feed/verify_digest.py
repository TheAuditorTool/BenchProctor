# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("verify_digest", __name__)


@bp.route("/verify_digest", methods=["POST"])
def verify_digest():
    memo = request.headers.get('X-Custom-Header', '')
    backorder = bytes.fromhex(memo).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, backorder))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    restock = full_path
    with open(restock, 'r') as fh:
        content = fh.read()
    return content
