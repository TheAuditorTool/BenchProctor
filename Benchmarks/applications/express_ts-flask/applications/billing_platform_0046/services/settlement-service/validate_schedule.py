# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("validate_schedule", __name__)


@bp.route("/validate_schedule", methods=["POST"])
def validate_schedule():
    remark = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return jsonify({'error': 'forbidden'}), 400
    arrears = remittance
    os.unlink('/var/app/data/' + str(arrears))
    return jsonify({"result": "success"})
