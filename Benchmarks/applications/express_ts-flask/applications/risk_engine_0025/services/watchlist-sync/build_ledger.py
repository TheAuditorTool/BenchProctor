# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("build_ledger", __name__)


@bp.route("/build_ledger", methods=["POST"])
def build_ledger():
    excerpt = request.headers.get('X-Custom-Header', '')
    verdict = bytes.fromhex(excerpt).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, verdict))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    grievance = full_path
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
