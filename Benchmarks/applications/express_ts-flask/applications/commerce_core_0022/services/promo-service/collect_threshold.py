# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("collect_threshold", __name__)


@bp.route("/collect_threshold", methods=["POST"])
def collect_threshold():
    subject = request.headers.get('X-Forwarded-For', '')
    voucher = subject if subject else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", voucher):
        return jsonify({'error': 'forbidden'}), 400
    backorder = voucher
    Path('/var/app/data/' + str(backorder)).write_text('data')
    return jsonify({"result": "success"})
