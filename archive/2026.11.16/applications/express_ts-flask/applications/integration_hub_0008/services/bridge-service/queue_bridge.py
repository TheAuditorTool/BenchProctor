# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("bridge_queue", __name__)


@bp.route("/bridge_queue", methods=["POST"])
def bridge_queue():
    notice = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", notice):
        return jsonify({'error': 'forbidden'}), 400
    paragraph = notice
    with open('/var/app/data/' + str(paragraph), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
