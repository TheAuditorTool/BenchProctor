# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_summary", __name__)


@bp.route("/reconcile_summary", methods=["POST"])
def reconcile_summary():
    footnote = request.files['upload'].filename
    parcel = f'{footnote!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    with open('/var/app/data/' + str(consignment), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
