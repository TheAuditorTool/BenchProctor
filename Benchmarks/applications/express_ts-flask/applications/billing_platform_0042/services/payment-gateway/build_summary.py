# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("build_summary", __name__)


@bp.route("/build_summary", methods=["POST"])
def build_summary():
    remark = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return jsonify({'error': 'forbidden'}), 400
    dunning = remittance
    os.unlink('/var/app/data/' + str(dunning))
    return jsonify({"result": "success"})
