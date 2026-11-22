# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("summarize_checkpoint", __name__)


@bp.route("/summarize_checkpoint", methods=["POST"])
def summarize_checkpoint():
    headline = request.headers.get('X-Forwarded-For', '')
    backorder = headline if headline else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    voucher = backorder
    Path('/var/app/data/' + str(voucher)).write_text('data')
    return jsonify({"result": "success"})
