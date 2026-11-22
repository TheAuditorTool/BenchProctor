# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_record", __name__)


@bp.route("/rotate_record", methods=["POST"])
def rotate_record():
    footnote = request.headers.get('X-Custom-Header', '')
    remittance = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, remittance))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    arrears = full_path
    with open(arrears, 'r') as fh:
        content = fh.read()
    return content
