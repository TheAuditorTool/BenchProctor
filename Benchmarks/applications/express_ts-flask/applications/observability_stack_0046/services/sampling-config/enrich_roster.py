# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_roster", __name__)


@bp.route("/enrich_roster", methods=["POST"])
def enrich_roster():
    paragraph = request.headers.get('X-Custom-Header', '')
    gauge = bytes.fromhex(paragraph).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, gauge))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    cohort = full_path
    with open(cohort, 'r') as fh:
        content = fh.read()
    return content
