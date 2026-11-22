# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("annotate_index", __name__)


@bp.route("/annotate_index", methods=["POST"])
def annotate_index():
    headline = request.headers.get('X-Custom-Header', '')
    disbursement = bytes.fromhex(headline).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, disbursement))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    remittance = full_path
    with open(remittance, 'r') as fh:
        content = fh.read()
    return content
