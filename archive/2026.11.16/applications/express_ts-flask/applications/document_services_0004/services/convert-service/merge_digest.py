# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_digest", __name__)


@bp.route("/merge_digest", methods=["POST"])
def merge_digest():
    excerpt = request.files['upload'].filename
    dossier = f'{excerpt!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", dossier):
        return jsonify({'error': 'forbidden'}), 400
    addendum = dossier
    with open('/var/app/data/' + str(addendum), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
