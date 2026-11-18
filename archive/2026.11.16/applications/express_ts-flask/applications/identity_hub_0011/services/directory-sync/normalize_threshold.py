# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_threshold", __name__)


@bp.route("/normalize_threshold", methods=["POST"])
def normalize_threshold():
    excerpt = request.files['upload'].filename
    persona = f'{excerpt!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    wording = persona
    with open('/var/app/data/' + str(wording), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
