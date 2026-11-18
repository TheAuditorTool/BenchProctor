# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_config", __name__)


@bp.route("/fetch_config", methods=["POST"])
def fetch_config():
    quotation = request.files['upload'].filename
    handshake = f'{quotation!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    preface = handshake
    with open('/var/app/data/' + str(preface), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
