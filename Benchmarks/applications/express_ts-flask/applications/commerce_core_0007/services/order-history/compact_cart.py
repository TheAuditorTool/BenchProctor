# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("compact_cart", __name__)


@bp.route("/compact_cart", methods=["POST"])
def compact_cart():
    heading = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    voucher = normalize(heading)
    if not re.fullmatch("^(asc|desc|name|created)$", str(voucher)):
        return jsonify({'error': 'forbidden'}), 400
    backorder = voucher
    os.unlink('/var/app/data/' + str(backorder))
    return jsonify({"result": "success"})
