# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("format_batch", __name__)


@bp.route("/format_batch", methods=["POST"])
def format_batch():
    summary = request.headers.get('X-Custom-Header', '')
    consignment = bytes.fromhex(summary).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, consignment))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    parcel = full_path
    with open(parcel, 'r') as fh:
        content = fh.read()
    return content
