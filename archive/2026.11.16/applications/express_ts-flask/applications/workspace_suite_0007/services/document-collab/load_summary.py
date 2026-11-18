# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("load_summary", __name__)


@bp.route("/load_summary", methods=["POST"])
def load_summary():
    summary = request.files['upload'].filename
    subtitle = f'{summary!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", subtitle):
        return jsonify({'error': 'forbidden'}), 400
    notice = subtitle
    with open('/var/app/data/' + str(notice), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
