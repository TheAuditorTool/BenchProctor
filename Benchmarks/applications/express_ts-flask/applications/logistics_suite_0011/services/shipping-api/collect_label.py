# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("collect_label", __name__)


@bp.route("/collect_label", methods=["POST"])
def collect_label():
    citation = request.headers.get('X-Forwarded-For', '')
    consignment = citation if citation else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", consignment):
        return jsonify({'error': 'forbidden'}), 400
    parcel = consignment
    Path('/var/app/data/' + str(parcel)).write_text('data')
    return jsonify({"result": "success"})
