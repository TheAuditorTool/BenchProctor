# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_window", __name__)


@bp.route("/merge_window", methods=["POST"])
def merge_window():
    notice = request.files['upload'].filename
    persona = f'{notice!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    with open('/var/app/data/' + str(handshake), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
