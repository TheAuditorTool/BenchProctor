# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("sync_watchlist", __name__)


@bp.route("/sync_watchlist", methods=["POST"])
def sync_watchlist():
    note = (request.get_json(silent=True) or {}).get("risk_payload", "")
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, note))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    grievance = full_path
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
