# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("render_config", __name__)


@bp.route("/render_config", methods=["POST"])
def render_config():
    heading = request.files['upload'].filename
    bulletin = f'{heading!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    excerpt = bulletin
    with open('/var/app/data/' + str(excerpt), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
