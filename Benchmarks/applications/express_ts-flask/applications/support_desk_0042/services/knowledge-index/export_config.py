# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("export_config", __name__)


@bp.route("/export_config", methods=["POST"])
def export_config():
    blurb = request.headers.get('X-Forwarded-For', '')
    inquiry = blurb if blurb else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    Path('/var/app/data/' + str(grievance)).write_text('data')
    return jsonify({"result": "success"})
