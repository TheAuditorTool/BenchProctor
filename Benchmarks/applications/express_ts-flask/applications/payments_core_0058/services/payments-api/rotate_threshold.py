# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("rotate_threshold", __name__)


@bp.route("/rotate_threshold", methods=["POST"])
def rotate_threshold():
    caption = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    ledger = normalize(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return jsonify({'error': 'forbidden'}), 400
    remittance = ledger
    os.unlink('/var/app/data/' + str(remittance))
    return jsonify({"result": "success"})
