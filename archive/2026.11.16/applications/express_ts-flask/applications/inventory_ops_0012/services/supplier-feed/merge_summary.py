# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_summary", __name__)


@bp.route("/merge_summary", methods=["POST"])
def merge_summary():
    phrase = request.files['upload'].filename
    backorder = f'{phrase!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    restock = backorder
    with open('/var/app/data/' + str(restock), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
