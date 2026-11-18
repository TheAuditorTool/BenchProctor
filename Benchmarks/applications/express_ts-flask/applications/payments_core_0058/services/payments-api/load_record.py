# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("load_record", __name__)


@bp.route("/load_record", methods=["POST"])
def load_record():
    caption = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    ledger = normalize(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return jsonify({'error': 'forbidden'}), 400
    remittance = ledger
    os.unlink('/var/app/data/' + str(remittance))
    return jsonify({"result": "success"})
