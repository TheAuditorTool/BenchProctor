# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("summarize_checkpoint", __name__)


@bp.route("/summarize_checkpoint", methods=["POST"])
def summarize_checkpoint():
    remark = request.headers.get('X-Forwarded-For', '')
    inquiry = remark if remark else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    Path('/var/app/data/' + str(grievance)).write_text('data')
    return jsonify({"result": "success"})
