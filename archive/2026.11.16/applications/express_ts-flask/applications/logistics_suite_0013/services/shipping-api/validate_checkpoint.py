# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_checkpoint", __name__)


@bp.route("/validate_checkpoint", methods=["POST"])
def validate_checkpoint():
    footnote = request.files['upload'].filename
    parcel = f'{footnote!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    with open('/var/app/data/' + str(consignment), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
