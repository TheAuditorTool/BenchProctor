# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_digest", __name__)


@bp.route("/summarize_digest", methods=["POST"])
def summarize_digest():
    summary = request.files['upload'].filename
    subtitle = f'{summary!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", subtitle):
        return jsonify({'error': 'forbidden'}), 400
    notice = subtitle
    with open('/var/app/data/' + str(notice), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
