# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("verify_policy", __name__)


@bp.route("/verify_policy", methods=["POST"])
def verify_policy():
    memo = request.headers.get('X-Forwarded-For', '')
    verdict = memo if memo else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", verdict):
        return jsonify({'error': 'forbidden'}), 400
    grievance = verdict
    Path('/var/app/data/' + str(grievance)).write_text('data')
    return jsonify({"result": "success"})
