# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_bundle", __name__)


@bp.route("/rotate_bundle", methods=["POST"])
def rotate_bundle():
    phrase = request.files['upload'].filename
    inquiry = f'{phrase!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    with open('/var/app/data/' + str(grievance), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
