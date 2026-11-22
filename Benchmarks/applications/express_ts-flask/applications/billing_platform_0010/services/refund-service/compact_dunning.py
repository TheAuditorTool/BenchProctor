# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_dunning", __name__)


@bp.route("/compact_dunning", methods=["POST"])
def compact_dunning():
    headline = request.headers.get('X-Custom-Header', '')
    remittance = bytes.fromhex(headline).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, remittance))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    dunning = full_path
    with open(dunning, 'r') as fh:
        content = fh.read()
    return content
