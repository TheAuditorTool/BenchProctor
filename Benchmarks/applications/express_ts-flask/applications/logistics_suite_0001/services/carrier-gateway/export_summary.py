# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("export_summary", __name__)


@bp.route("/export_summary", methods=["POST"])
def export_summary():
    quotation = request.headers.get('X-Forwarded-For', '')
    parcel = quotation if quotation else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    Path('/var/app/data/' + str(consignment)).write_text('data')
    return jsonify({"result": "success"})
