# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_roster", __name__)


@bp.route("/validate_roster", methods=["POST"])
def validate_roster():
    preface = request.files['upload'].filename
    handshake = f'{preface!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    paragraph = handshake
    with open('/var/app/data/' + str(paragraph), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
